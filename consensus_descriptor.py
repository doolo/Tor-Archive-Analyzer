from stem.descriptor import DocumentHandler
from stem.descriptor import parse_file
import glob

# for consensus in glob.glob('./archive/consensuses/*'):
for consensus in glob.glob('./archive/per_month_consensuses/**/*consensus', recursive=True):
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
            role = []
            if 'Guard' in desc.flags:
                role.append('Guard')
            if 'Exit' in desc.flags:
                role.append('Exit')
            if len(role) == 0:
                continue
            elif len(role) == 1:
                role = role[0]
            elif len(role) == 2:
                role = "GE"
                # role = 'Middle'
            print(desc.fingerprint, \
                  desc.published, \
                  # desc.flags, \
                  role,)
