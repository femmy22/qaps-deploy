import React, { useState, useEffect, useContext  } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import classes from './TestCompleted.module.css';
import DataContext from '../../DataContext';

function TestCompleted() {
    const [sessionID, setSessionID] = useState('');
    // const {data} = useContext(DataContext);
    // const navigate = useNavigate();

    const handleDownloadPdf = async () => {
        try {
            // const response = await fetch('http://localhost:5000/generate_pdf_report', {
            const response = await fetch('http://ec2-34-224-180-254.compute-1.amazonaws.com/api/generate_pdf_report', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ session_id: sessionID }),
            });
            if (response.ok) {

                const blob = await response.blob();
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = sessionID +"_session.pdf";
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                window.URL.revokeObjectURL(url);
                // After downloading, navigate to the '/thank-you' route
                // navigate('/generate_pdf_report');
            } else {
                console.error('Failed to fetch PDF:', response.statusText);
            }
        } catch (error) {
            console.error('Error downloading PDF:', error);
        }
    };

    const handleSessionIDChange = (event) => {
        setSessionID(event.target.value);
    };


    return (
        <div className={classes.reportSearch}>
			<Modal>
				<Link className={classes.homepage} to="/">
					<p>Return to Homepage</p>
				</Link>
        <div className="testCompleted">
            <h1>Test Completed</h1>
            <p>Thank you for completing the prewriting test!</p>
            <p>
                <label>
                    Enter Session ID: 
                    <input type="text" value={sessionID} onChange={handleSessionIDChange} />
                </label>
            </p>
            <p>
                <Link className={classes.link} onClick={handleDownloadPdf}>Download PDF Report</Link>
            </p>
        </div>
        </Modal>
    </div>
    );
}

export default TestCompleted;











// import React from 'react';
// import { useState } from 'react';
// import { Link, useNavigate } from 'react-router-dom';
// import classes from './TestCompleted.module.css';

// function TestCompleted() {
//     const [pdfLink, setPdfLink] = useState('');

//     // Function to generate PDF dynamically and set the link
//     const generatePdf = async () => {
//         try {
//             // Call the server endpoint to generate the PDF
//             const response = await fetch('/generate-pdf');
//             if (response.ok) {
//                 // If successful, get the URL of the generated PDF
//                 const pdfUrl = await response.text();
//                 setPdfLink(pdfUrl); // Set the PDF link
//             } else {
//                 console.error('Failed to generate PDF:', response.statusText);
//             }
//         } catch (error) {
//             console.error('Error generating PDF:', error);
//         }
//     };

//     return (
//         <div className="testCompleted">
//             <h1>Test Completed</h1>
//             <h2>Thank you for completing the prewriting test!</h2>
//             <p>
//                 <Link className={classes.link} download onClick={generatePdf}>
//                     Download PDF Report
//                 </Link>
//             </p>
//         </div>
//     );
// }

// export default TestCompleted;
