import Box from '@mui/material/Box';

export default function PageView(props) {
  console.log("page view props: ", props);

  return (
    <Box  sx={{ width: '100%', maxWidth: 1000, height: 800, bgcolor: 'orange' }}>

      {props.component}
    </Box>
  )
}