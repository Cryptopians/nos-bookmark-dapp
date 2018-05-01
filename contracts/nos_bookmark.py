from boa.builtins import concat
from boa.code.builtins import list
from boa.interop.Neo.Runtime import CheckWitness, GetTrigger, Log
from boa.interop.Neo.Storage import Delete, Get, GetContext, Put
from boa.interop.Neo.TriggerType import Application, Verification
from boa.interop.System.ExecutionEngine import GetCallingScriptHash


def Main(operation, args):
    """Main definition of the nOS Bookmark dApp Smart Contract.

    :param operation: str The name of the operation to perform
    :param args: list A list of arguments along with the operation
    :return: bytearray: The result of the operation
    """
    # TODO: Carefully read http://neo-boa.readthedocs.io/en/latest/overview.html#what-parts-of-python-are-supported
    address_from = args[0]

    # Verify if the address we want to operate from is the invoking address
    is_owner = CheckWitness(address_from)

    if not is_owner:
        Log("Must be the owner of the address")
        return False

    # Crud operations
    if operation == 'AddBookmark':
        return True

    if operation == 'SetBookmark':
        return True

    if operation == 'DeleteBookmark':
        return True

    # Share operations
    if operations == 'ShareBookmark':
        return True

    if operation == 'ShareAllBookmarks':
        return True

    if operation == 'ApproveBookmark':
        return True

    if operation == 'RejectBookmark':
        return True

    return False
