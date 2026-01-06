import axios from 'axios';
import styles from './home.module.css'; 
import { useEffect, useState } from 'react';
import { useNavigate , useLocation} from "react-router-dom";
import { Link } from 'react-router-dom';
import Cookies from 'js-cookie'
import add from './addicon.png';
import subtract from './subtract.png';

export default function Billing(){
     const API_URL = process.env.REACT_APP_API_URL;
    const [tickets,setTickets] = useState(0)
    const [amount,setAmount] = useState(0)
    const { state } = useLocation()
     const navigate = useNavigate()
     console.log(state)
    const  show_id = state.show_id 
    const Amount = state.price  * tickets
    const increment = async(tickets) => {
        setTickets(tickets+1)   
        
    }

    const decrement = async(tickets) => {
        if (tickets>0){
        setTickets(tickets-1)
      
        
        }      
    }

      const getTickets = async() =>{
  const res = await axios.post(`${API_URL}bookings/`,{show : show_id,total_tickets : tickets,Amount : Amount},{
    withCredentials : true,
    headers : {
      "Content-Type" :  "application/json",
        'X-CSRFToken' : Cookies.get('csrftoken')
    }
  })
 console.log("data ",res.data)
  navigate(`/bookings/`)
}

    return (
        <div>
            <h2>Movie : {state.title}</h2>
            <p>Theater : {state.theater} </p>
            <p>Show : {state.show} PM</p>
            {/* <p>Billing</p> */}
              <label style={{marginRight : "5px"}}>No. of tickets</label>
         <img src={subtract}   width={20} onClick={() => decrement(tickets)} style={{marginRight : "5px"}}/>
        <input type="number" min={1} onChange={(e) => setTickets(e.target.value)} value={tickets} style={{marginRight : "5px"}} />
        <img src={add}   width={20} onClick={() => increment(tickets)} />
         <p>Ticket Price : {state.price} </p>
          <p>Total Tickets : {tickets} </p>
        <p>Total Amount : {Amount} </p>
         <button onClick={getTickets}>Book tickets</button> 
        </div>
    )
}