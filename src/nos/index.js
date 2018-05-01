import nos from "@nosplatform/api-functions/es6"
import React from "react"

const { Provider, Consumer } = React.createContext(nos)

const injectNOS = Component => props => (
  <Consumer>{context => <Component nos={context} {...props} />}</Consumer>
)

export { Provider, Consumer, injectNOS }
