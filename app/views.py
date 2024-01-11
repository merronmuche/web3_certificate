from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

def view_certificate(request, trainee_id):
    # Example data - in a real application, you would retrieve this from your database
    trainee_name = "John Doe"  # You would fetch this using trainee_id
    challenge_name = "Web3 Development Challenge"
    nft_id = "NFT123456789"
    blockchain_url = "https://explorer.algorand.org/transaction/" + nft_id

    # Context to be passed to the template
    context = {
        'trainee_name': trainee_name,
        'challenge_name': challenge_name,
        'nft_id': nft_id,
        'blockchain_url': blockchain_url,
    }

    # Render and return the template
    return render(request, 'certificates/view_certificate.html', context)
