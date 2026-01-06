
// import './App.css';im
import Login from './components/Login';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Register from './components/Register';
import Home from './components/home';
import Theaters from './components/Theaters';
import Theater from './components/Theater';
import Confirmation from './components/confirmation';
import MyBookings from './components/MyBookings';
import Shows from './components/shows';
import Billing from './components/billing';
import ProtectedRoute from './components/ProtectedRoute';

function App() {
  return (
    <div className="App">
    <Router>
      <Routes>
        <Route path='/login' element={<Login></Login>}></Route>
        <Route path='/' element={<Register></Register>}></Route>
        <Route path='/home' element={<Home></Home>}></Route>
        <Route path='/theaters' element={<Theaters></Theaters>}></Route>
        <Route path='/theaters/:id' element={<Theater></Theater>}></Route>
        <Route path='/bookings' element={<Confirmation></Confirmation>}></Route>
         <Route path='/mybookings' element={<MyBookings></MyBookings>}></Route>
           <Route path='/movies/:movieId/theaters' element={<Shows></Shows>}></Route>
            <Route path='/billing' element={<Billing></Billing>}></Route>
      </Routes>
    </Router>
      {/* <h1>React</h1> */}
     
    </div>
  );
}

export default App;
