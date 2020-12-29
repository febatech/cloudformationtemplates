with open('netapp_vpcid_pubsubnet_params') as f:
    a=f.read()
    vpc_id=a.split("\n")[0]
    vpc_public_subnet_ids_0=a.split("\n")[1]





hidden_values=[
        {
        'ParameterKey': 'CloudManagerPassword',
            'ParameterValue': 'FebaTech$123'
        },
        {
        'ParameterKey': 'CloudManagerUserEmail',

            'ParameterValue': 'awspearls@febatech.com'
        },
        {
        'ParameterKey': 'CompanyName',

            'ParameterValue': 'FebaTech'
        },
        {
        'ParameterKey': 'KeyPair',

            'ParameterValue': 'guru'
        },
        {
        'ParameterKey': 'QSS3BucketName',

            'ParameterValue': 'febatech-project-pocs'
        },
        {
        'ParameterKey': 'QSS3KeyPrefix',

            'ParameterValue': 'netapp-cvo-sunjay/quickstart-netapp-ontapcloud-sql'
        },
        {
        'ParameterKey': 'RemoteAccessCIDR',

            'ParameterValue': '0.0.0.0/0'
        },
       {
                'ParameterKey': 'VPCCIDR',
                'ParameterValue': '172.18.0.0'
        },
        {
        'ParameterKey': 'VPCId',

            'ParameterValue': vpc_id
        },
        {
        'ParameterKey': 'SubnetId',

            'ParameterValue': vpc_public_subnet_ids_0
        },

        ]