import './App.css';
import { useEffect, useState } from 'react';
// import { fetchTimeForHelloWorld } from './api/APIUtils'
import Dashboard from './components/Dashboard';
import Header from './components/Header';
import Footer from './components/Footer';

function App() {
  // const [currentTime, setCurrentTime] = useState(0);

  // useEffect(() => {
  //   fetchTimeForHelloWorld().then(response => {
  //     setCurrentTime(response.time);
  //   })
  // })

  return (
    <div className="App">
      <Header />
      <Dashboard />
      <Footer />
    </div>
  );
}

export default App;
