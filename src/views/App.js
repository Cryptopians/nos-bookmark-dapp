import React from 'react'

import { injectNOS } from '../nos'

class App extends React.PureComponent {
  constructor () {
    super()

    this.state = {
      address: undefined
    }
  }

  async componentDidMount () {
    if (this.props.nos.exists) {
      const address = await this.props.nos.getAddress()

      this.setState({ address })
    }
  }

  render () {
    return (
      <div>
        <h1>nOS SSO dApp</h1>
        {!this.props.nos.exists && (
          <p>Please view this dApp within your nOS client</p>
        )}
        {this.state.address && (
          <p>Your address: {this.state.address}</p>
        )}
      </div>
    )
  }
}

export default injectNOS(App)
