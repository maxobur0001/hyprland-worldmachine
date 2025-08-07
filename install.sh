dir="$(dirname $0)"

mv ~/.config/fastfetch ~/.config/fastfetch.old
ln -sf "$dir/fastfetch" ~/.config/fastfetch

mv ~/.config/hypr ~/.config/hypr.old
ln -sf "$dir/hypr" ~/.config/hypr
hyprctl reload

mv ~/.config/kitty ~/.config/kitty.old
ln -sf "$dir/kitty" ~/.config/kitty

mv ~/.config/rofi ~/.config/rofi.old
ln -sf "$dir/rofi" ~/.config/rofi

mv ~/.config/waybar ~/.config/waybar.old
ln -sf "$dir/waybar" ~/.config/waybar
killall waybar
setsid waybar

mv ~/.config/dunst ~/.config/dunst.old
ln -sf "$dir/dunst" ~/.config/dunst
killall dunst

mv ~/.config/qutebrowser ~/.config/qutebrowser.old
ln -sf "$dir/qutebrowser" ~/.config/qutebrowser

echo "Link to all directories from worldmachine/ added to ~/.config, old files marked with *.old"
