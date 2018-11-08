from stem.descriptor import DocumentHandler
from stem.descriptor import parse_file
import glob

for consensus in glob.glob('./archive/consensuses/*'):
    # In theory, when we need to check if the flag is in the
    # known_flags set, before testing it against all the
    # relays. However, since Valid, Guard and Exit are supported since
    # the beginning of the Tor network, we do not need to take care of
    # this case.

    # for desc in parse_file(consensus,   \
    #     descriptor_type = 'network-status-consensus-3 1.0', \
    #     document_handler = DocumentHandler.DOCUMENT,):
    #     print(desc.known_flags)
    for desc in parse_file(consensus):
        if 'Valid' in desc.flags:
            if 'Guard' in desc.flags:
                role = 'Guard'
            elif 'Exit' in desc.flags:
                role = 'Exit'
            else:
                role = 'Middle'
            print(desc.fingerprint, \
                  desc.published, \
                  # desc.flags, \
                  role,)
