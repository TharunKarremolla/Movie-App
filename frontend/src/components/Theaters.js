import { useState, useEffect } from "react";
import axios from 'axios';
import { useNavigate, useLocation} from "react-router-dom";


export default function Theaters(){
    const API_URL = process.env.REACT_APP_API_URL;
    const { state } = useLocation();
    const [time,setTime] = useState()
    const [theaters,setTheaters] = useState([])
    const navigate = useNavigate()

    const getTheaters = async() => {
  const res = await axios.get(`${API_URL}shows/`,{"id" : state.id})
  setTheaters(res.data.data)
  setTime(res.data.time)
   
    }

  
useEffect(() => {
  getTheaters();
},[])
    return (
        <div>
 <h1>Theaters</h1>
             <ul>
        {theaters.map((theater) => (
            <div key={theater.id}>
            <h3>title : {theater.name}</h3>
            <p>location : {theater.location}</p>
            <p>capacity : {theater.capacity}</p>
              {/* <p>language : {movie.language}</p>
                <img src={movie.poster}></img>
            <p>rating : {movie.rating}</p> */}
            <button onClick={() => navigate(`/theaters/${theater.id}`,{ state : { id : state.id,movie_name : state.movie_name }})} >Show Timing</button>
            </div>
          
        ))}
       </ul>
        </div>
       
    )
}