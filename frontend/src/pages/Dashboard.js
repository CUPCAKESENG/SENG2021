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

  const getInvoices = () => {
    axios.get('http://localhost:5000/invoice/list', {params: {token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywibmFtZSI6ImpvaG5hcHBsZXNlZWQiLCJ3aWxkY2FyZCI6LTQ5ODgsImV4cCI6MTY0OTY4MzEwMX0.8uHJv6OByXdVho0VdDHqasFVIrGFj7x2zROFiJPXe74'}})
      .then(res => {
        console.log("list: ", res);
      })
  }

  return (
    <>
      <text>Dashboard</text>
      <button onClick={handleButtonClick}>Test Button</button>
      <button onClick={getInvoices}>Get invoices</button>
      <BasicList />
    </>
  )
}