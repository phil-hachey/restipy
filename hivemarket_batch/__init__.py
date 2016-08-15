import json, click, boto3

from service import KmsService, JwtService, HiveMarketService

@click.group()
@click.option('-p', '--profile',
    default='default',
    help='AWS shared profile to use.')
@click.option('--private-key',
    envvar='PRIVATE_KEY',
    help='Private key to sign the processing token.')
@click.option('--token-expiry',
    envvar='TOKEN_EXPIRY',
    default=10000,
    help='TTL for processing token.')
@click.option('--token-signing-algorithm',
    envvar='TOKEN_SIGNING_ALGORITHM',
    default='HS256',
    help='Token encryption algorithm.')
@click.option('--api-url',
    envvar='API_URL',
    help='API server URL.')
@click.pass_context
def main(ctx, profile, private_key, token_expiry, token_signing_algorithm, api_url):
    session = boto3.Session(profile_name=profile)
    
    kmsService = KmsService(session=session)
    private_key = kmsService.decrypt(private_key)
    
    jwtService = JwtService(
        private_key=private_key,
        token_expiry=token_expiry,
        token_signing_algorithm=token_signing_algorithm
        )
    token = jwtService.encode({
        'type': 'processing'
    })
    
    hive_market_service = HiveMarketService(
        api_url=api_url,
        token=token)
    
    ctx.obj = {
        'hive_market_service': hive_market_service
    }

@main.command()
@click.pass_context
def send_reoccuring(ctx):
    hive_market_service = ctx.obj['hive_market_service']
    response = hive_market_service.send_reoccuring()
    print json.dumps(response.json())

if __name__ == '__main__':
    main()
