import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Modal from '../../components/modal/Modal';
import classes from './ReportSearch.module.css';


function ReportSearch() {
    const [sessionID, setSessionID] = useState('');
    
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
				<Link className={classes.button} to="/">
					<p>Return to Homepage</p>
				</Link>
        <div className="reportSearch">
            <h1>Search for reports</h1>
        
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

export default ReportSearch;











