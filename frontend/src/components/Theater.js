import { useState, useEffect } from "react";
import axios from 'axios';
import Cookies from 'js-cookie';
import { useNavigate, useLocation} from "react-router-dom";
import styles from './Register.module.css';
import { useParams } from "react-router-dom";


export default function Theater(){
     const API_URL = process.env.REACT_APP_API_URL;

    const [theater,setTheater] = useState([])
     const [shows,setShows] = useState([])
    const params = useParams()
    const [tickets,setTickets] = useState(0)
    const { state } = useLocation()   
      const [selectedShow, setSelectedShow] = useState(null);
      const navigate = useNavigate()
    

    const getTheater = async() => {
  const res = await axios.get(`${API_URL}theaters/${params.id}`)
  setTheater(res.data.data)

    }

     const getShows = async() => {
  const res = await axios.get(`${API_URL}shows/`)
    setShows(res.data.shows)

    }

const getTickets = async() =>{
  const res = await axios.post(`${API_URL}bookings/`,{show : selectedShow ,total_tickets : tickets},{
    withCredentials : true,
    headers : {
      "Content-Type" :  "application/json",
        'X-CSRFToken' : Cookies.get('csrftoken')
    }
  })
 console.log(res.data)
  navigate(`/bookings/`)
}   
  
useEffect(() => {
  getTheater();
  getShows();
},[])


    return (
        <div>
 <h1>Theaters</h1>
    
      <h2>Movie : {state.movie_name}</h2>
       <h3>Theater : {theater.name}</h3>
        <p>location : {theater.location}</p>
        <p>capacity : {theater.capacity}</p>
        <p>Show Time :</p>
          {shows.map((show) => (
            <div key={show.id}>
              <button                onClick={() => setSelectedShow(show.id)}
style={{
                margin: "8px",
                padding: "10px",
                backgroundColor:
                  selectedShow === show.id ? "red" : "lightgray",
                color: "white",
                border: "none",
                cursor: "pointer"
              }} >{show.start_time}</button>
            </div>
          ))} 
        <label>Number of tickets</label>
        
        <input type="text" onChange={(e) => setTickets(e.target.value)} />
        

        <button onClick={getTickets}>Book tickets</button>
        
         
        
   
        </div>
       
    )
}