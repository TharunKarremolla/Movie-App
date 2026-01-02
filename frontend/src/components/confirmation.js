import { useState,useEffect } from "react";
import axios from 'axios';
import Cookies from 'js-cookie';
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";

axios.defaults.withCredentials = true; 

export default function Confirmation(){
   const [data,setData] = useState({})
   const API_URL = process.env.REACT_APP_API_URL;

       const myBookings = async() => {
        try{
  const res = await axios.get(`${API_URL}bookings/`)
      
        setData(res.data.message[0])
        }
        catch(error){
            console.log(error)
        }
    }

 useEffect(() => {
   myBookings();
   
 },[])

    return (
        <div>
            {Object.keys(data).length>0  ? (<>
           <h2>Tickets Booked</h2>
           <Link to='/MyBookings' >My Bookings</Link>
           <h2>Movie  : {data.movie}</h2>
           <h2>Theater : {data.theater}</h2>
           <h2>TotalTickets :{data.total_tickets}</h2>
           <h2>Show Time :{data.show}</h2>
           </>) : (<h1>No Bookings are Made</h1>)}
        </div>
    )
}