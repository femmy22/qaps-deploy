import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

import sys
import re
from io import BytesIO

# Function to sanitize session ID for file naming
def sanitize_session_id(session_id):
    # Replace characters that are not alphanumeric or underscores with underscores
    sanitized_session_id = re.sub(r'[^a-zA-Z0-9_]', '_', session_id)
    return sanitized_session_id

# Function to generate PDF report based on session IDs
def generate_pdf_report(session_id, host, database, user, password, port):
    # Connect to the database
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        if connection.is_connected():
            print("Connected to MySQL database")

            # Prepare a cursor object using cursor() method
            cursor = connection.cursor()

            # Fetch data for the provided session ID and all other session IDs
            query = "SELECT sessionID, score FROM norm"
            cursor.execute(query)
            combined_data = pd.DataFrame(cursor.fetchall(), columns=['sessionID', 'score'])

            # Close the cursor
            cursor.close()

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        return

    finally:
        # Close the connection
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

    if combined_data.empty:
        print("No data found in the database.")
        return

    # Create PDF buffer
    buffer = BytesIO()

    # Create PDF document
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Add title
    title_style = ParagraphStyle(name='TitleStyle', fontSize=24, leading=30)
    title = "Prewriting Report"
    elements.append(Paragraph(title, title_style))
    elements.append(Spacer(1, 12))

    # Add subtitle
    subtitle_style = ParagraphStyle(name='SubtitleStyle', fontSize=16, leading=20)
    subtitle = "Session ID: {}".format(session_id)
    elements.append(Paragraph(subtitle, subtitle_style))
    elements.append(Spacer(1, 12))

    # Add subsubtitle (custom style)
    subsubtitle_style = ParagraphStyle(name='SubsubtitleStyle', fontSize=12, leading=14)
    subsubtitle = "Clinician Only"
    elements.append(Paragraph(subsubtitle, subsubtitle_style))
    elements.append(Spacer(1, 12))

    # Add table showing session ID and corresponding score
    table_data = [['Session ID', 'Score']]
    table_data.append([session_id, combined_data[combined_data['sessionID'] == session_id]['score'].iloc[0]])
    elements.append(Table(table_data))

    # Step 3: Create a bell curve plot using matplotlib
    fig, ax = plt.subplots()

    # Plot histogram for all session IDs
    ax.hist(combined_data['score'], bins=25, density=True, alpha=0.6, color='b')

    # Fit a normal distribution to the data
    mu = combined_data['score'].mean()
    sigma = combined_data['score'].std()
    xmin, xmax = combined_data['score'].min(), combined_data['score'].max()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, sigma)

    # Plot the bell curve
    ax.plot(x, p, 'k', linewidth=2)

    # Highlight the score of the provided session ID
    session_scores = combined_data[combined_data['sessionID'] == session_id]['score']
    ax.scatter(session_scores, norm.pdf(session_scores, mu, sigma), label=session_id, color='red', marker='o')

    # Set plot labels and legend
    ax.set_title('Bell Curve')
    ax.set_xlabel('Score')
    ax.set_ylabel('Frequency')
    ax.legend()

    # Convert plot to bytes
    imgdata = BytesIO()
    fig.savefig(imgdata, format='png')
    imgdata.seek(0)

    # Add the bell curve plot to the PDF
    img = Image(imgdata)
    img.drawHeight = 3*inch
    img.drawWidth = 5*inch
    elements.append(img)

    # Build the PDF
    doc.build(elements)

    # Get the PDF content from buffer
    pdf_data = buffer.getvalue()
    buffer.close()

    # Write PDF content to a file
    filename = 'session_{}.pdf'.format(sanitize_session_id(session_id))
    with open(filename, 'wb') as f:
        f.write(pdf_data)
    print("PDF saved as:", filename)
    return pdf_data

if __name__ == "__main__":
    # Check if session ID is provided as argument
    if len(sys.argv) < 2:
        print("Usage: python generate_pdf_report.py <session_id>")
        sys.exit(1)

    # Define database connection information
    # host = "cmsc508.com"
    # database = "22FA_team32"
    # user = "shieldsn"
    # password = "V01000930"
    
    host = "aws-test-1.c5wcy2ag81s4.us-east-2.rds.amazonaws.com"
    database = "23fa_test"
    user = "admin"
    password = 'Capstone24'
    port = "3306"

    # Get session ID from command-line argument
    session_id = sys.argv[1]

    # Generate PDF report
    generate_pdf_report(session_id, host, database, user, password)

