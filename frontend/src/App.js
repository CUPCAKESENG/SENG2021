import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';



function App() {

  let testResponse;

  const testFunction = () => {
    if(testResponse){
      return testResponse;
    }
    testResponse = fetch('http://localhost:5000/register', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: "test1@email.com",
        password: "testPassword",
        firstname: "Bob",
        lastname: "Jim"
      })
    }).then(response => {
        console.log("testing: ");
        console.log(response.json())
      })
      .then(response => {
        console.log("test response: ", response);
        return response;
      })
      .catch(error => console.log(error));

    // this is a promise right now
    return testResponse;
  }

  const asyncRequest = async () => {
    
  }

  useEffect(()=>{
    // fetch('http://localhost:5000/test',{
    //   'methods':'GET',
    //   headers : {
    //     'Content-Type':'application/json',
    //     'Accept': 'application/json'
    //   }
    // })
    // .then(response => response.json())
    // .then(response => console.log("response: ", response))
    // .catch(error => console.log(error))

    const response = asyncRequest();
    console.log("a: ", response);

  },[])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
