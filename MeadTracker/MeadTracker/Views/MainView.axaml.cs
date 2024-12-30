using Avalonia.Controls;
using Avalonia.Interactivity;
using System;
using System.Diagnostics;

namespace MeadTracker.Views;

public partial class MainView : UserControl
{
    public MainView()
    {
        InitializeComponent();
    }

    public void CalculateTemputureClicked(object source, RoutedEventArgs e)
    {
        Debug.WriteLine($"CLICK! Celsius = {celsius.Text}");
        float Tf = (Convert.ToSingle(celsius.Text) * (9/5)) + 32;
        fahrenheit.Text = Tf.ToString();
    }
}
