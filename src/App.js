import './App.css';
import { useEffect, useState } from 'react';
// import { fetchTimeForHelloWorld } from './api/APIUtils'
import Dashboard from './components/Dashboard';
import Header from './components/Header';
import Footer from './components/Footer';

function App() {
  return (
    <div className="min-h-screen">
      <Header />
      <Dashboard />
      <Footer />
    </div>
  );
}

export default App;
