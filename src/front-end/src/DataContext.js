import React, { createContext, useState } from 'react';

// Create a context
const DataContext = createContext(null);

// Create a provider component
// export const MyProvider = ({ children }) => {
//   const [data, setData] = useState(null);

//   return (
//     <DataContext.Provider value={{ data, setData }}>
//       {children}
//     </DataContext.Provider>
//   );
// };

// Custom hook to consume the context
export default DataContext;