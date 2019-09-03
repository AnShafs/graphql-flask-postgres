from graphql_relay.node.node import from_global_id

def input_to_dictionary(input):
    # convert Graphene inputs into dictionary
    output = {}
    for key in input:
        # convert GraphQL global id to database id
        if key[-2:] == 'id':
            input[key] = from_global_id(input[key])[1]
        output[key] = input[key]
    return output