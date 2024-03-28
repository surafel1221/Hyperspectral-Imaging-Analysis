import matplotlib.pyplot as plt
from spectral import *
from matplotlib.widgets import Slider

def load_dispaly_Cube(image_path):
    img= open_image(image_path).load()
    initial_band = 0
    
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.25, bottom=0.25)  # Adjust subplot to make room for the slider
    
    band_display = plt.imshow(img[:, :, initial_band], cmap='gray')
    ax.set_title(f'Band {initial_band+1}')
    
    ax_band = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    band_slider = Slider(
        ax=ax_band,
        label='Band',
        valmin=0,
        valmax=img.shape[2]-1,  # Max band index
        valinit=initial_band,
        valstep=1
    )
    
    def update(val):
        band = band_slider.val
        band_display.set_data(img[:, :, band])
        ax.set_title(f'Band {band+1}')
        fig.canvas.draw_idle()
    
    band_slider.on_changed(update)
    
    plt.show()

