import { Routes, Route, BrowserRouter } from "react-router-dom";
import React, { Suspense } from "react";
import { AnimatePresence } from 'framer-motion'
 
import Navbar from './components/Navbar'
import Home from './pages/Home'
import Plan from './pages/Plan'
import Completed from './pages/Completed'

import './App.css';


function App() {
  return (
    <div className="App">
    <BrowserRouter>
        <Suspense fallback={<div>Page Loading...</div>}>
        <AnimatePresence
         mode='wait'>
           <Routes>
             <Route path="/" exact element={<Home />} />
             <Route path="/plan" exact element={<Plan />} />
             <Route path="/completed" exact element={<Completed />} />
           </Routes>
        </AnimatePresence>
        </Suspense>
    </BrowserRouter>
  </div>
  );
}

export default App;