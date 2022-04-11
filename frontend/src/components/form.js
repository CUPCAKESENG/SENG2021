import React, { Fragment, useState } from 'react';

import ButtonGroup from '@atlaskit/button/button-group';
import LoadingButton from '@atlaskit/button/loading-button';
import Button from '@atlaskit/button/standard-button';
import { Checkbox } from '@atlaskit/checkbox';
import TextField from '@atlaskit/textfield';
import axios from 'axios';

import Form, {
  CheckboxField,
  ErrorMessage,
  Field,
  FormFooter,
  FormHeader,
  FormSection,
  HelperMessage,
  ValidMessage,
} from '@atlaskit/form';

const FormDefaultExample = (props) => {
  

  const handleChangeUsername = (data) => {
    const registrationDetails = {
      username: data.username,
      password: data.password
    }

    const loginCred = {
      email: data.username,
      password: data.password
    }

    let result = axios.post('http://localhost:5000/login', loginCred)
    .then(res => {
      console.log("result: ", res);

      return res;
    })

    console.log(`The saved result is ${result}`);
    console.log('Testing 1, 2');

    console.log(`The saved result is ${result}`);
    console.log(`The saved result is ${result}`);
    console.log(`The saved result is ${result}`);
    console.log(`The saved result is ${result}`);


    console.log(`\n\nThe username is ${data.username.toUpperCase()}\n\n`);
    props.onChange(registrationDetails);

    // if res
    // props.gotoRegister('/dashboard');
  };

  const handleRedirectRegister = () => {
    console.log("props: ", props);
    props.gotoRegister('/register');
  }

  return (<div
    style={{
      display: 'flex',
      width: '400px',
      maxWidth: '100%',
      margin: '0 auto',
      flexDirection: 'column',
    }}
  >
    <Form
      onSubmit={(data) => {
        handleChangeUsername(data);

        return new Promise((resolve) => setTimeout(resolve, 2000)).then(() =>
          data.username === 'error' ? { username: 'IN_USE' } : undefined,
        );
      }}
    >
      {({ formProps, submitting }) => (
        <form {...formProps}>
          <FormHeader
            title="Sign in"
          />
          <FormSection>
            <Field
              aria-required={true}
              name="username"
              label="Username"
              isRequired
              defaultValue="dst12"
            >
              {({ fieldProps, error }) => (
                <Fragment>
                  <TextField autoComplete="off" {...fieldProps} />
                  {error && (
                    <ErrorMessage>
                      This username is already in use, try another one.
                    </ErrorMessage>
                  )}
                </Fragment>
              )}
            </Field>
            <Field
              aria-required={true}
              name="password"
              label="Password"
              defaultValue=""
              isRequired
              validate={(value) =>
                value && value.length < 8 ? 'TOO_SHORT' : undefined
              }
            >
              {({ fieldProps, error, valid, meta }) => {
                return (
                  <Fragment>
                    <TextField type="password" {...fieldProps} />
                    {error && !valid && (
                      <HelperMessage>
                        Use 8 or more characters with a mix of letters, numbers
                        and symbols.
                      </HelperMessage>
                    )}
                    {error && (
                      <ErrorMessage>
                        Password needs to be more than 8 characters.
                      </ErrorMessage>
                    )}
                  </Fragment>
                );
              }}
            </Field>
            <CheckboxField name="remember" label="Remember me" defaultIsChecked>
              {({ fieldProps }) => (
                <Checkbox
                  {...fieldProps}
                  label="Always sign in on this device"
                />
              )}
            </CheckboxField>
          </FormSection>
          
          <Button appearance="subtle-link" style={{position: "relative", top:58, left:-12}} onClick={handleRedirectRegister}>Register</Button>
          <FormFooter>
            
            <ButtonGroup>
              <Button appearance="subtle">Cancel</Button>
              <LoadingButton
                type="submit"
                appearance="primary"
                isLoading={submitting}
              >
                Sign up
              </LoadingButton>
            </ButtonGroup>
          </FormFooter>
        </form>
      )}
    </Form>
  </div>
  );
}

export default FormDefaultExample;