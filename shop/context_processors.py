from .models import Cart

def cart_items_count(request):
    """Context processor to provide cart item count to all templates."""
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            return {'cart_items_count' : cart.get_total_items()}
        except Cart.DoesNotExist:
            # Fixed: Added missing return statement - was returning None before
            return {'cart_items_count' : 0}
    return {'cart_items_count' : 0}