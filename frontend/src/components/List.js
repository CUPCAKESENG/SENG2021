import * as React from 'react';
import Box from '@mui/material/Box';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Divider from '@mui/material/Divider';
import InboxIcon from '@mui/icons-material/Inbox';
import DraftsIcon from '@mui/icons-material/Drafts';
import DashboardIcon from '@mui/icons-material/Dashboard';
import ReceiptLongIcon from '@mui/icons-material/ReceiptLong';
import FaceIcon from '@mui/icons-material/Face';
import LogoutIcon from '@mui/icons-material/Logout';

export default function BasicList(props) {
  const handleDashboardClick = () => {
    console.log('Dashboard clicked');
    props.setViewDashboard(true);
    props.setViewTransactions(false);
    props.setViewAccount(false);
  }
  const handleTransactionsClick = () => {
    console.log('Transactions clicked');
    props.setViewDashboard(false);
    props.setViewTransactions(true);
    props.setViewAccount(false);
  }
  const handleManageCountClick = () => {
    console.log('ManageAccount clicked');
    props.setViewDashboard(false);
    props.setViewTransactions(false);
    props.setViewAccount(true);
  }
  const handleLogoutClick = () => {
    console.log('Logout clicked');
  }
  return (
    <Box sx={{ width: '100%', maxWidth: 250, height: 800, bgcolor: 'green' }}>
      <nav aria-label="main mailbox folders">
        <List>
          <ListItem disablePadding onClick={handleDashboardClick}>
            <ListItemButton>
              <ListItemIcon>
                <DashboardIcon />
              </ListItemIcon>
              <ListItemText primary="Dashboard" />
            </ListItemButton>
          </ListItem>
          <ListItem disablePadding onClick={handleTransactionsClick}>
            <ListItemButton>
              <ListItemIcon>
                <ReceiptLongIcon />
              </ListItemIcon>
              <ListItemText primary="Transactions" />
            </ListItemButton>
          </ListItem>
          <ListItem disablePadding onClick={handleManageCountClick}>
            <ListItemButton>
              <ListItemIcon>
                <FaceIcon />
              </ListItemIcon>
              <ListItemText primary="Manage account" />
            </ListItemButton>
          </ListItem>
          <ListItem disablePadding onClick={handleLogoutClick}>
            <ListItemButton>
              <ListItemIcon>
                <LogoutIcon />
              </ListItemIcon>
              <ListItemText primary="Logout" />
            </ListItemButton>
          </ListItem>
        </List>
      </nav>
      
    </Box>
  );
}
