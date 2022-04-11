import BasicList from "../components/List";
import axios from 'axios';

export const Dashboard = () => {

  const handleButtonClick = () => {
    console.log("button clicked");
    const loginCred = {
      email: "hey@gmail.com",
      password: "hey124"
    }
    // make the post request to the backend
    axios.post('http://localhost:5000/login', loginCred)
      .then(res => {
        console.log("result: ", res);
      })
  }

  return (
    <>
      <text>Dashboard</text>
      <button onClick={handleButtonClick}>Test Button</button>
      <BasicList />
    </>
  )
}