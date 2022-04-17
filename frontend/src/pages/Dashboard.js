import BasicList from "../components/List";
import axios from 'axios';
import { useState } from "react";
import { Transactions } from "./Transactions";
import { DashboardData } from "./DashboardData";
import { ManageAccount } from "./ManageAccount";
import PageView from "../components/PageView";
import { Grid } from '@material-ui/core';

export const Dashboard = () => {
  const [viewDashboard, setViewDashboard] = useState(true);
  const [viewTransactions, setViewTransactions] = useState(false);
  const [viewAccount, setViewAccount] = useState(false);

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
    <Grid container justify='flex-end'>
      
      <BasicList setViewDashboard={setViewDashboard} setViewTransactions={setViewTransactions} setViewAccount={setViewAccount}/>

      <PageView />

      {viewDashboard && (
        <DashboardData />
      )}

      {viewTransactions && (
        <Transactions />
      )}

      {viewAccount && (
        <ManageAccount />
      )}

      <button onClick={handleButtonClick}>Test Button</button>
      <button onClick={getInvoices}>Get invoices</button>
    </Grid>
  )
}

const dashboardLayoutStyle = {
  flexDirection: 'row'
}