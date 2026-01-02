import { useState,useEffect } from "react";
import axios from 'axios';
import Cookies from 'js-cookie';
import { useNavigate } from "react-router-dom";
import styles from "./Login.module.css";
import { Link } from "react-router-dom";

axios.defaults.withCredentials = true; 

export default function MyBookings(){   
       const API_URL = process.env.REACT_APP_API_URL;

    const [Tickets,setTickets] = useState([])
     const navigate = useNavigate()


    const myBookings = async() => {

        try{
  const res = await axios.get(`${API_URL}bookings/`)
  setTickets(res.data.message)
        }
        catch(error){
            console.log(error.data)
        }


    }
   

useEffect(() => {
  myBookings();
},[])

    return (
        <div>
 <h1>Bookings</h1>
         {Tickets ?( <ul>
         {Tickets.map((ticket) => (
            <div key={ticket.booking_id}>
            <h3>Movie : {ticket.movie}</h3>
            <p>Theater : {ticket.theater}</p>
            <p>Show : {ticket.show}</p>
             <p>Tickets : {ticket.total_tickets}</p>
              
          
            {/* <button onClick={() => navigate(`/theaters/${theater.id}`,{ state : { id : state.id,movie_name : state.movie_name }})} >Show Timing</button> */}
            </div>
        
        ))}
       </ul> ) : <h3>No Bookings were Made</h3> }
        </div> ) }