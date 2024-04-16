// App.js is a standard React feature. Google it to learn what it does.
// In short, nothing in the front-end would work without it.

import { createContext, useState } from 'react';
import { Route, Routes } from 'react-router-dom';
import Overlay from './components/overlay/Overlay';
import Login from './pages/login/Login';
import Home from './pages/home/Home';
import Records from './pages/records/Records';
import Instructions from './pages/instructions/Instructions';
import Circle from './pages/evaluations/Circle';
import DoubleLine from './pages/evaluations/DoubleLine';
import TripleLine from './pages/evaluations/TripleLine';
import SingleLine from './pages/evaluations/SingleLine';
import VerticalLine from './pages/evaluations/VerticalLine';
import Square from './pages/evaluations/Square';
import MiniVerticalLines from './pages/evaluations/MiniVerticalLines';
import UnsymmetricalLines from './pages/evaluations/UnsymmetricalLines';
import PlusSign from './pages/evaluations/PlusSign';
import Triangle from './pages/evaluations/Triangle';
import Report from './pages/report/Report';
import Redraw from './pages/evaluations/Redraw';


// Contexts allow for values to be shared between different components
export const TestSession = createContext(); // Stores the test session ID
export const RecordStorage = createContext(); // Stores the last table that was searched in the records page.
export const LeftHanded = createContext(); // Stores data on whether the user is left or right handed.

function App() {
	// Allow for the contexts above to be changed.
	const [testSessionId, updateTestSessionId] = useState('');
	const [records, updateRecordsStored] = useState(undefined);
	const [leftHanded, updateDominantHand] = useState(false);

	// Sets the current state of the child to be the entered name
	function onNameChangeHandler(sessionId) {
		updateTestSessionId(sessionId);
	}

	// Updates the most previous table that was searched in the records page.
	function storeRecordsHandler(storedRecords) {
		updateRecordsStored(storedRecords);
	}

	// Updates whether or not the user is left handed or right handed.
	function updateDominantHandHandler(dominantHand) {
		updateDominantHand(dominantHand);
	}

	return (
		<Overlay>
			<TestSession.Provider value={{ testSessionId }}>
				<RecordStorage.Provider value={{ records }}>
					<LeftHanded.Provider value={{ leftHanded }}>
						<Routes>
							<Route path="/login" element={<Login />}></Route>
							<Route
								path="/"
								element={<Home onNameChange={onNameChangeHandler} />}
							></Route>
							<Route
								path="/records"
								element={<Records storeRecords={storeRecordsHandler} />}
							></Route>
							<Route path="/redraw" element={<Redraw />}></Route>
							<Route
								path="/new-evaluation"
								element={
									<Instructions
										onNameChange={onNameChangeHandler}
										onHandChange={updateDominantHandHandler}
									/>
								}
							></Route>
							<Route path="/new-evaluation/circle" element={<Circle />}></Route>
							<Route
								path="/new-evaluation/double-line"
								element={<DoubleLine />}
							></Route>
							<Route
								path="/new-evaluation/triple-line"
								element={<TripleLine />}
							></Route>
							<Route path="/new-evaluation/square" element={<Square />}></Route>
							<Route
								path="/new-evaluation/single-line"
								element={<SingleLine />}
							></Route>
							<Route
								path="/new-evaluation/vertical-line"
								element={<VerticalLine />}
							></Route>
							<Route
								path="/new-evaluation/mini-vertical-lines"
								element={<MiniVerticalLines />}
							></Route>
							<Route
								path="/new-evaluation/unsymmetrical-lines"
								element={<UnsymmetricalLines />}
							></Route>
							<Route
								path="/new-evaluation/plus-sign"
								element={<PlusSign />}
							></Route>
							<Route
								path="/new-evaluation/triangle"
								element={<Triangle />}
							></Route>
							{/* <Route path="/report" element={<Report />}></Route> */}
							<Route
								path="/report/report"
								element={<Report />}
							></Route>
						</Routes>
					</LeftHanded.Provider>
				</RecordStorage.Provider>
			</TestSession.Provider>
		</Overlay>
	);
}

export default App;


// src/index.js

// import React from 'react';
// import ReactDOM from 'react-dom';
// import { BrowserRouter as Router, Route } from 'react-router-dom'; // Import the necessary routing components
// import ReportPage from './Report'; // Import your new component

// ReactDOM.render(
//   <Router>
//     <Route path="/" exact component={ReportPage} />
//     <Route path="/view-report" render={() => <div>Report will be displayed here</div>} />
//   </Router>,
//   document.getElementById('root')
// );
