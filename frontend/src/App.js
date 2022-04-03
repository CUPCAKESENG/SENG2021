import { SignIn } from './SignIn';
import { Dashboard } from './Dashboard';
import { Register } from './Register';
import { useState, useEffect } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

function App() {

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [firstName, setFirstname] = useState('');
  const [lastName, setLastname] = useState('');

  const [registerDetails, setRegisterDetails] = useState({}); 

  const [counter, setCounter] = useState(0);
  const [isRegistered, setIsRegistered] = useState(false);


  useEffect(() => {
    console.log("updated");
    console.log(registerDetails);
  }, [registerDetails]);

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/register' element={<Register />}/>
          <Route path='/' element={<SignIn onChange={setRegisterDetails} testing={'test prop'}/>} />
          <Route path='/dashboard' element={<Dashboard />} />
        </Routes>
      </BrowserRouter>
      
    </>
  );
}

export default App;
