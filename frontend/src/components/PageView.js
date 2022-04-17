import Box from '@mui/material/Box';
import { useState } from 'react';

export default function PageView(props) {
  console.log("page view props: ", props);
  const [windowDimensions, setWindowDimensions] = useState(getWindowDimensions());

  function getWindowDimensions() {
    const { innerWidth: width, innerHeight: height } = window;
    console.log("dimensions: ", width, height)
    return {
      width,
      height
    };
  }

  return (
    <Box  sx={{ width: '75%', maxWidth: windowDimensions.width, height: windowDimensions.height, bgcolor: 'background.paper' }}>

      {props.component}
      
    </Box>
  )
}