import { SignIn } from './pages/SignIn';
import { Dashboard } from './pages/Dashboard';
import { Register } from './pages/Register';
import { useState, useEffect } from 'react';
import { BrowserRouter, Route, Routes, useNavigate } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Root />
    </BrowserRouter>
  )
  
}

function Root() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [firstName, setFirstname] = useState('');
  const [lastName, setLastname] = useState('');

  const [registerDetails, setRegisterDetails] = useState({}); 

  const [counter, setCounter] = useState(0);
  const [isRegistered, setIsRegistered] = useState(false);

  const navigate = useNavigate();

  useEffect(() => {
    console.log("updated");
    console.log(registerDetails);
  }, [registerDetails]);

  return (
    <>
      <Routes>
        <Route path='/register' element={<Register navigate={navigate}/>}/>
        <Route path='/' element={<SignIn onChange={setRegisterDetails} testing={'test prop'} gotoRegister={navigate}/>} />
        <Route path='/dashboard' element={<Dashboard />} />
      </Routes>
    </>
  );
}


export default App;
