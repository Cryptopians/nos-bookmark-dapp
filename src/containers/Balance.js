import React from 'react'

import { injectNOS } from '../nos'

class Balance extends React.PureComponent {
  constructor () {
    super()

    this.state = {
      balance: 0
    }
  }

  async componentDidMount () {
    if (this.props.nos.exists) {
      const balance = await this.props.nos.getBalance('c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b')

      this.setState({ balance })
    }
  }

  render () {
    if (!this.props.nos.exists) {
      return null
    }

    return (
      <div>
        Balance: {this.state.balance} NEO
      </div>
    )
  }
}

export default injectNOS(Balance)
