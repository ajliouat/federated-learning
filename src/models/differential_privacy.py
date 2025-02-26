from opacus import PrivacyEngine

def apply_differential_privacy(model, optimizer, sample_rate, noise_multiplier, max_grad_norm):
    privacy_engine = PrivacyEngine()
    model, optimizer, _ = privacy_engine.make_private(
        module=model,
        optimizer=optimizer,
        data_loader=None,
        noise_multiplier=noise_multiplier,
        max_grad_norm=max_grad_norm,
        batch_size=sample_rate
    )
    return model, optimizer