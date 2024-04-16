import React, { useState, useContext, useEffect } from 'react'; 
import {Link, useNavigate} from 'react-router-dom';
import { TestSession } from '../../App';
import { Document, Page, pdfjs } from 'react-pdf'; // Import Document, Page, and pdfjs
import classes from './Report.module.css';

pdfjs.GlobalWorkerOptions.workerSrc = `https://cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.min.js`;

function Report(props) {
   const navigate = useNavigate();
   const [numPages, setNumPages] = useState(null);
   const [pageNumber, setPageNumber] = useState(1);
   const testSession = useContext(TestSession); // The test session ID that was used for the evaluation

   const onDocumentLoadSuccess = ({ numPages }) => {
    setNumPages(numPages);
  };

  //  const pdf = '/sample.pdf'; // Change the path to your PDF
   const openPdf = () => {
    window.open("/sample.pdf");
  };

  useEffect(() => {
		const dataBaseQuery = {
			table: 'score',
			shape: 'Any',
			session: testSession,
		};
		const token = sessionStorage.getItem('Security Token');

		// Sending POST request to URL
		const URL = 'http://localhost:5000/get-data';
		// 	const URL = 'http://3.238.55.170:5000/get-data';  // AWS server

		fetch(URL, {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`,
			},
			body: JSON.stringify(dataBaseQuery),
		})
			.then((response) => response.json())
      // definitely look here for what data looks like from back-end
			.then((data) => {
        console.log(data);

        
        /**
         * Score Table reference
         * 
         * CREATE TABLE score(
        sessionID VARCHAR(255),
        straightness DOUBLE(5,3),
        equilaterality DOUBLE(5,3),
        alignment DOUBLE(5,3),
        roundness DOUBLE(5,3),
        closure DOUBLE(5,3),
        spacing DOUBLE(5,3),
        lineRatio DOUBLE(5,3),
        bisection DOUBLE(5,3),
        bisectionAngle DOUBLE(5,3),
        score DOUBLE(5,3),
        PRIMARY KEY(sessionID)
        );
        
        */
       
        // console.log(data.straightness);
        // TODO: send object data to pdf

				// data.table = enteredTable;
				// Removing -1s from table; changing them to 0s
				// for (let i = 0; i < data.length; i++) {
				// 	for (let j = 1; j < data[i].length; j++) {
				// 		if (data[i][j] < 0) {
				// 			data[i][j] = 0;
				// 			if (data.table === 'score') data[i][10] += 1;
				// 		}
				// 	}
				// }

				// const dataObject = {
				// 	table: data.table,
				// 	records: data,
				// };
				// props.storeRecords(dataObject);
				// updateDataDisplay(dataObject);
				// updateTableRender(true);
			});

  }, []) 

  return (
    <div>
      <h1>Report</h1>
      <Document
        file="/sample.pdf"
        onLoadSuccess={onDocumentLoadSuccess}
      >
        <Page pageNumber={pageNumber} />
      </Document>
      <p>
        Page {pageNumber} of {numPages}
      </p>
      <button onClick={openPdf}>View Report</button>
    </div>
  );
  }
  
  export default Report;
  
  //  useEffect(() => {
	// 	props.onNameChange(undefined);
	// 	const token = sessionStorage.getItem('Security Token');
	// 	if (token == null || token === 'undefined') {
	// 		navigate('/login');
	// 	}
	// });

  // const pdf = "sample.pdf";

//   return (
//     <div className={classes.report}>
//       <div className={classes.selection}>
//         <Link className={classes.link} to="./sample.pdf">
//           View Report
//         </Link>
//         {/* <button className={classes.link} onClick={() => window.open(pdf, '_blank')}>Open PDF</button> */}
//         {/* <Document
//           file={pdf}
//           onLoadSuccess={onDocumentLoadSuccess}
//         >
//           <Page pageNumber={pageNumber} />
//         </Document> */}
//       </div>
//       <p className={classes.message}>
//         Note: You must save your evaluations to view the report later.
//       </p>
//     </div>
//   );
// }

// export default Report;

// function MainComponent() {
//   const [showReport, setShowReport] = useState(false);

//   const toggleReport = () => {
//     setShowReport(!showReport);
//   };

//   return (
//     <div className={classes.report}>
//       <div className={classes.selection}>
//         <a className={classes.link} onClick={toggleReport}>
//           View Report
//         </a>
//         <div style={{ display: showReport ? 'block' : 'none' }}>
//           <Report />
//         </div>
//       </div>
//       <p className={classes.message}>
//         Note: You must save your evaluations to view the report later.
//       </p>
//     </div>
//   );
// }

// export default {Report, MainComponent};




