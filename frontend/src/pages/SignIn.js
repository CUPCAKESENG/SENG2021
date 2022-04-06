import FormDefaultExample from "../components/form"
import Button from '@atlaskit/button/standard-button';

export const SignIn = (props) => {
  console.log("props: ", props);
  return (
    <>
      <FormDefaultExample onChange={props.onChange} gotoRegister={props.gotoRegister}/>  
    </>
    
  )
}