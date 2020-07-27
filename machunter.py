# Import libraries for extra functionality.
from pprint import pprint                       # PrettyPrinting
import netmiko                                  # Network device CLI handling
from ntc_templates.parse import parse_output    # Turn CLI output into structured data

# Define the network device. The netmiko library cares about this object.
# https://ktbyers.github.io/netmiko/#tutorialsexamplesgetting-started
network_device = {
    'device_type': 'cisco_ios',
    'host':   '172.22.46.1',
    'username': 'demo',
    'password': 'notverysecure',
}

# We defined the network device, so let's open a socket aka connection to it.
socket = netmiko.ConnectHandler(**network_device)

# Let's define the command we're sending to the CLI as a variable since we're
# using it in more than one place.
the_cli_command = 'show mac address-table'

# Send the command to the network device CLI over the socket.
# Save the unstructured result.
cli_output_blob = socket.send_command(the_cli_command)

# Using the ntc_templates library, let's parse the unstructured result.
# Save the parsed result, which should be structured data.
cli_output_structured = parse_output(platform="cisco_ios", command=the_cli_command, data=cli_output_blob)

# PrettyPrint the data structure that the ntc_templates library made for us.
pprint(cli_output_structured,indent=4)
