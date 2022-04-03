import React, { Fragment, useState } from 'react';

import ButtonGroup from '@atlaskit/button/button-group';
import LoadingButton from '@atlaskit/button/loading-button';
import Button from '@atlaskit/button/standard-button';
import { Checkbox } from '@atlaskit/checkbox';
import TextField from '@atlaskit/textfield';

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

export const RegisterForm = (props) => {
  
  const handleRegistration = (data) => {
    console.log("handling registration");
    console.log(data);
    props.navigate("/dashboard");
  }
  return (
    <div
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

          handleRegistration(data);
          return new Promise((resolve) => setTimeout(resolve, 2000)).then(() =>
            data.username === 'error' ? { username: 'IN_USE' } : undefined,
          );
        }}
      >
        {({ formProps, submitting }) => (
          <form {...formProps}>
            <FormHeader
              title="Register"
            />
            <FormSection>
              <Field
                aria-required={true}
                name="username"
                label="Username"
                isRequired
                defaultValue=""
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
              <Field
                aria-required={true}
                name="firstname"
                label="First name"
                isRequired
                defaultValue=""
              >
                {({ fieldProps, error }) => (
                  <Fragment>
                    <TextField autoComplete="off" {...fieldProps} />
                  </Fragment>
                )}
                
              </Field>

              <Field
                aria-required={true}
                name="lastname"
                label="Last name"
                isRequired
                defaultValue=""
              >
                {({ fieldProps, error }) => (
                  <Fragment>
                    <TextField autoComplete="off" {...fieldProps} />
                  </Fragment>
                )}
                
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
            
            <FormFooter>
              
              <ButtonGroup>
                <Button appearance="subtle">Cancel</Button>
                <LoadingButton
                  type="submit"
                  appearance="primary"
                  isLoading={submitting}
                >
                  Register
                </LoadingButton>
              </ButtonGroup>
            </FormFooter>
          </form>
        )}
      </Form>
    </div>
  )
}