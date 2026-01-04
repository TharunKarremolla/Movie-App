import axios from 'axios';
import styles from './home.module.css'; 
import { useEffect, useState } from 'react';
import { useNavigate } from "react-router-dom";
import { Link } from 'react-router-dom';
import Cookies from 'js-cookie'


export default function Home( {user}) {
    const API_URL = process.env.REACT_APP_API_URL
    const [movies,setMovies] = useState([])
    const [time,setTime] = useState()
    const navigate = useNavigate();

 

const getMovies = async() => {
  const res = await axios.get(`${API_URL}movies/`)
setMovies(res.data.data)
setTime(res.data.time)
console.log(res.data)
}

const handleLogout = async() => {
  
  const res = await axios.post(`${API_URL}auth/logout/`,{},{
    withCredentials : true,
    headers : {
      "Content-Type" : 'application/json',
      'X-CSRFToken' : Cookies.get('csrftoken')

    }
  }  )

navigate('/login')
}



useEffect(() => {
  getMovies();
},[])

  return (
    <div className={styles.main}>
      
       <h1>Home</h1>
     <Link to='/MyBookings' >My Bookings</Link>
     <button onClick={handleLogout}>Logout</button>
       <ul>
        {movies.map((movie) => (
            <div key={movie.id}>
            <h3>Title : {movie.title}</h3>
            <p>Description : {movie.description}</p>
              <p>Language : {movie.language}</p>
                <img width={250} height={200} src={movie.poster}></img>
            <p>rating : {movie.rating}</p>
            <button onClick={() => navigate(`/movies/${movie.id}/theaters`, {state : {id: movie.id,movie_name : movie.title}})} >Book tickets</button>
            </div>
          
        ))}
       </ul>
     
        </div>
   
  );
}