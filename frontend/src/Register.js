import { RegisterForm } from "./components/registerForm"

export const Register = (props) => {
  return (
    <>
      <RegisterForm navigate={props.navigate}/>
    </>
  )
}