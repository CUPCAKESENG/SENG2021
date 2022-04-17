import BasicList from "../components/List";
import axios from 'axios';
import { useState, useEffect } from "react";
import { Transactions } from "./Transactions";
import { DashboardData } from "./DashboardData";
import { ManageAccount } from "./ManageAccount";
import PageView from "../components/PageView";
import { Grid } from '@material-ui/core';

export const Dashboard = () => {
  const [viewDashboard, setViewDashboard] = useState(true);
  const [viewTransactions, setViewTransactions] = useState(false);
  const [viewAccount, setViewAccount] = useState(false);

  useEffect(() => {
    console.log('useeffect triggered');
  }, [viewDashboard, viewTransactions, viewAccount])
  
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
    
      <Grid container justify='flex-end' width='100vw' height='100vh' >
        
        <BasicList setViewDashboard={setViewDashboard} setViewTransactions={setViewTransactions} setViewAccount={setViewAccount}/>

        {viewDashboard && <PageView component={<DashboardData />}/>}
        {viewTransactions && <PageView component={<Transactions />}/>}
        {viewAccount && <PageView component={<ManageAccount />}/>}
        
      </Grid>
    </>
    
  )
}

const dashboardLayoutStyle = {
  flexDirection: 'row'
}

const gridStyle = {
  container: true,
  width: '100vw',
  height: '100vh',
  spacing: 0,
  justify: 'flex-end'
}