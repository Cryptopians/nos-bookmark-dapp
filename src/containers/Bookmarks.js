import { u, wallet } from '@cityofzion/neon-js'
import { str2hexstring, int2hex, hexstring2str } from '@cityofzion/neon-js/src/utils'
import { unhexlify } from 'binascii'
import React from 'react'

import { injectNOS } from '../nos'

const SC_SCRIPT_HASH = '0x218a962c8072cd349a4a98532d86a0734067b8c1'

const addressToScriptHash = (address) => unhexlify(u.reverseHex(wallet.getScriptHashFromAddress(address)))

class Bookmarks extends React.PureComponent {
  constructor () {
    super()

    this.state = {
      results: []
    }
  }

  async componentDidMount () {
    if (this.props.nos.exists) {
      try {
        const address = await this.props.nos.getAddress()
        const bookmarks = this.props.nos.testInvoke(SC_SCRIPT_HASH, 'GetBookmarks', [str2hexstring(address)])

        this.setState({ bookmarks })
      } catch (error) {
        console.error(error)
      }
    }
  }

  render () {
    if (!this.props.nos.exists) {
      return null
    }

    return (
      <div>
        Bookmarks: {this.state.results.length}
      </div>
    )
  }
}

export default injectNOS(Bookmarks)
