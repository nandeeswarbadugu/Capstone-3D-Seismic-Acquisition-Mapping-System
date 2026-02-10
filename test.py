import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from seismic_acquisition import SeismicAcquisitionApp  # Update the import to the actual module

class TestSeismicAcquisitionApp(unittest.TestCase):
    
    @patch('seismic_acquisition.messagebox.showinfo')
    @patch('seismic_acquisition.messagebox.showerror')
    @patch('matplotlib.pyplot.show')
    @patch('seismic_acquisition.Document')  # Mock the Document class
    def test_plot_seismic_data(self, mock_Document, mock_show, mock_showerror, mock_showinfo):
        root = tk.Tk()
        app = SeismicAcquisitionApp(root)

        # Provide valid inputs
        app.entry_x_extent.insert(0, '100')
        app.entry_y_extent.insert(0, '100')
        app.entry_gx_distance.insert(0, '10')
        app.entry_gx_line_distance.insert(0, '10')
        app.entry_sx_distance.insert(0, '10')
        app.entry_sx_line_distance.insert(0, '10')

        # Call the plot method
        app.plot_seismic_data()

        # Assert matplotlib's `show` was called for plotting
        mock_show.assert_called()

    @patch('seismic_acquisition.messagebox.showinfo')
    @patch('seismic_acquisition.messagebox.showerror')
    @patch('seismic_acquisition.Document')  # Mock the Document class
    def test_save_multiplicity_success(self, mock_Document, mock_showerror, mock_showinfo):
        root = tk.Tk()
        app = SeismicAcquisitionApp(root)

        # Provide valid inputs
        app.entry_x_extent.insert(0, '100')
        app.entry_y_extent.insert(0, '100')
        app.entry_gx_distance.insert(0, '20')
        app.entry_gx_line_distance.insert(0, '15')
        app.entry_sx_distance.insert(0, '15')
        app.entry_sx_line_distance.insert(0, '20')

        # Mock Document and file saving
        mock_document_instance = MagicMock()
        mock_Document.return_value = mock_document_instance

        # Call save_multiplicity
        app.save_multiplicity()

        # Assert messagebox success was called
        mock_showinfo.assert_called()

    @patch('seismic_acquisition.messagebox.showinfo')
    @patch('seismic_acquisition.messagebox.showerror')
    @patch('seismic_acquisition.Document')  # Mock the Document class
    def test_save_multiplicity_error(self, mock_Document, mock_showerror, mock_showinfo):
        root = tk.Tk()
        app = SeismicAcquisitionApp(root)

        # Provide valid inputs
        app.entry_x_extent.insert(0, '100')
        app.entry_y_extent.insert(0, '100')
        app.entry_gx_distance.insert(0, '10')
        app.entry_gx_line_distance.insert(0, '10')
        app.entry_sx_distance.insert(0, '10')
        app.entry_sx_line_distance.insert(0, '10')

        # Mock a save error
        mock_document_instance = MagicMock()
        mock_Document.return_value = mock_document_instance
        mock_document_instance.save.side_effect = Exception("File save error")

        # Call save_multiplicity
        app.save_multiplicity()

        # Assert error messagebox was called
        mock_showerror.assert_called_with("Error", "An error occurred while saving the file: File save error")

    @patch('seismic_acquisition.messagebox.showinfo')
    @patch('seismic_acquisition.messagebox.showerror')
    def test_invalid_input(self, mock_showerror, mock_showinfo):
        root = tk.Tk()
        app = SeismicAcquisitionApp(root)

        # Provide invalid inputs
        app.entry_x_extent.insert(0, '-1')  # Invalid: Negative value
        app.entry_y_extent.insert(0, 'abc')  # Invalid: Non-numeric
        app.entry_gx_distance.insert(0, '0')  # Invalid: Zero
        app.entry_gx_line_distance.insert(0, '10')
        app.entry_sx_distance.insert(0, '10')
        app.entry_sx_line_distance.insert(0, '10')

        # Call plot_seismic_data
        app.plot_seismic_data()

        # Assert error message was shown
        mock_showerror.assert_called()

class CustomTextTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"✔ {test._testMethodName} - Success")

class CustomTextTestRunner(unittest.TextTestRunner):
    resultclass = CustomTextTestResult

if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner())

