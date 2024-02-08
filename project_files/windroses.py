import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#________________________________________________________________________YEARLY WINDROSES________________________________________________________________________

def create_yearly_windrose():

    file_path = "csv_files\\windrose_csv_data\\wind_data_yearly.csv"

    # Read the CSV data using the updated file path
    data = pd.read_csv(file_path, header=None, skiprows=1, names=['Year', 'Id_Estacao', 'dicofre', 'Concelho', 'Direction', 'Min', 'Max', 'Average'], encoding='utf-8')

    direction_mapping = {
        1.0: 0,
        2.0: 45.0,
        3.0: 90.0,
        4.0: 135.0,
        5.0: 180.0,
        6.0: 225.0,
        7.0: 270.0,
        8.0: 315.0
    }

    data['Direction'] = data['Direction'].map(direction_mapping)

    # Create a Windrose plot for each unique combination of Year, Month, and Concelho
    for (year, concelho), group in data.groupby(['Year', 'Concelho']):
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(20, 10))

        # Set directional labels
        ax.set_theta_direction(-1)
        ax.set_theta_offset(0.5 * np.pi)
        ax.set_xticks(np.linspace(0, 2*np.pi, 8, endpoint=False))  # Adjust ticks for radians

        # Set custom direction labels
        direction_labels = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        ax.set_xticklabels(direction_labels)

        # Compute normalization limits for each windrose individually
        norm_min = 0
        norm_max = group[['Min', 'Average', 'Max']].max().max()
        combined_norm = plt.Normalize(norm_min, norm_max)

        # Plot three sets of bars for min, max, and average with manual radial positioning
        theta = group['Direction'].values * np.pi / 180  # Convert to radians
        ax.bar(
            theta,
            group['Min'],
            width=0.3,
            color=plt.cm.viridis(combined_norm(group['Min'])),
            edgecolor='white',
            alpha=0.7,
            label='_nolegend_'
        )
        ax.bar(
            theta,
            group['Average'] - group['Min'],  # Adjusting the height to overlap with Min
            width=0.3,
            color=plt.cm.viridis(combined_norm(group['Average'])),
            edgecolor='white',
            alpha=0.7,
            bottom=group['Min'],
            label='_nolegend_'
        )
        ax.bar(
            theta,
            group['Max'] - group['Average'],  # Adjusting the height to overlap with Average
            width=0.3,
            color=plt.cm.viridis(combined_norm(group['Max'])),
            edgecolor='white',
            alpha=0.7,
            bottom=group['Average'],
            label='_nolegend_'
        )

        # Manually adjust radial position for overlaying bars
        ax.set_rmax(norm_max * 1.1)

        cbar = plt.colorbar(
            plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=combined_norm),
            ax=ax,
            pad=0.1,
            orientation='vertical',  # Change to 'horizontal' if needed
            aspect=20,  # Adjust the aspect ratio as needed
            shrink=0.8  # Adjust the shrink factor as needed
        )
        cbar.set_label('Wind Speed [m/s]')

        plt.title(f'{concelho} - {year}', fontsize=20, y=1.05)
        file_name = (f'{group["dicofre"].iloc[0]}_{concelho}_{year}.png')
        plt.savefig(os.path.join('year_windroses', file_name), dpi=300, bbox_inches='tight', pad_inches=0.1)
        plt.close(fig)


#________________________________________________________________________MONTHLY WINDROSES________________________________________________________________________

def create_monthly_windrose():

    file_path = "csv_files\\windrose_csv_data\\wind_data_monthly.csv"

    # Read the CSV data using the updated file path
    data = pd.read_csv(file_path, header=None, skiprows=1, names=['Month', 'Id_Estacao', 'dicofre', 'Concelho', 'Direction', 'Min', 'Max', 'Average'], encoding='utf-8')

    direction_mapping = {
        1.0: 0,
        2.0: 45.0,
        3.0: 90.0,
        4.0: 135.0,
        5.0: 180.0,
        6.0: 225.0,
        7.0: 270.0,
        8.0: 315.0
    }

    data['Direction'] = data['Direction'].map(direction_mapping)

    # Create a Windrose plot for each unique combination of Year, Month, and Concelho
    for (month, concelho), group in data.groupby(['Month', 'Concelho']):
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(20, 10))

        # Set directional labels
        ax.set_theta_direction(-1)
        ax.set_theta_offset(0.5 * np.pi)
        ax.set_xticks(np.linspace(0, 2*np.pi, 8, endpoint=False))  # Adjust ticks for radians

        # Set custom direction labels
        direction_labels = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        ax.set_xticklabels(direction_labels)

        # Compute normalization limits for each windrose individually
        norm_min = 0
        norm_max = group[['Min', 'Average', 'Max']].max().max()
        combined_norm = plt.Normalize(norm_min, norm_max)

        # Plot three sets of bars for min, max, and average with manual radial positioning
        theta = group['Direction'].values * np.pi / 180  # Convert to radians
        ax.bar(
            theta,
            group['Min'],
            width=0.3,
            color=plt.cm.viridis(combined_norm(group['Min'])),
            edgecolor='white',
            alpha=0.7,
            label='_nolegend_'
        )
        ax.bar(
            theta,
            group['Average'] - group['Min'],  # Adjusting the height to overlap with Min
            width=0.3,
            color=plt.cm.viridis(combined_norm(group['Average'])),
            edgecolor='white',
            alpha=0.7,
            bottom=group['Min'],
            label='_nolegend_'
        )
        ax.bar(
            theta,
            group['Max'] - group['Average'],  # Adjusting the height to overlap with Average
            width=0.3,
            color=plt.cm.viridis(combined_norm(group['Max'])),
            edgecolor='white',
            alpha=0.7,
            bottom=group['Average'],
            label='_nolegend_'
        )

        # Manually adjust radial position for overlaying bars
        ax.set_rmax(norm_max * 1.1)

        cbar = plt.colorbar(
            plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=combined_norm),
            ax=ax,
            pad=0.1,
            orientation='vertical',  # Change to 'horizontal' if needed
            aspect=20,  # Adjust the aspect ratio as needed
            shrink=0.8  # Adjust the shrink factor as needed
        )
        cbar.set_label('Wind Speed [m/s]')

        month_mapping = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }

        actual_month = month_mapping[month]
        plt.title(f'{concelho} - {actual_month}', fontsize=20, y=1.05)
        file_name = (f'{group["dicofre"].iloc[0]}_{concelho}_{actual_month}.png')
        plt.savefig(os.path.join('month_windroses', file_name), dpi=300, bbox_inches='tight', pad_inches=0.1)
        plt.close(fig)

#________________________________________________________________________YEAR AND MONTH WINDROSES________________________________________________________________________

def create_year_month_windrose():

    file_path = "csv_files\\windrose_csv_data\\wind_data_year_month.csv"

    # Read the CSV data using the updated file path
    data = pd.read_csv(file_path, header=None, skiprows=1, names=['Month', 'Year', 'Id_Estacao', 'dicofre', 'Concelho', 'Direction', 'Min', 'Max', 'Average'], encoding='utf-8')

    direction_mapping = {
        1.0: 0,
        2.0: 45.0,
        3.0: 90.0,
        4.0: 135.0,
        5.0: 180.0,
        6.0: 225.0,
        7.0: 270.0,
        8.0: 315.0
    }

    data['Direction'] = data['Direction'].map(direction_mapping)

    # Create a Windrose plot for each unique combination of Year, Month, and Concelho
    for (year, month, concelho), group in data.groupby(['Year', 'Month', 'Concelho']):
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(20, 10))

        # Set directional labels
        ax.set_theta_direction(-1)
        ax.set_theta_offset(0.5 * np.pi)
        ax.set_xticks(np.linspace(0, 2*np.pi, 8, endpoint=False))  # Adjust ticks for radians

        # Set custom direction labels
        direction_labels = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        ax.set_xticklabels(direction_labels)

        # Compute normalization limits for each windrose individually
        norm_min = 0
        norm_max = group[['Min', 'Average', 'Max']].max().max()
        combined_norm = plt.Normalize(norm_min, norm_max)

        # Plot three sets of bars for min, max, and average with manual radial positioning
        theta = group['Direction'].values * np.pi / 180  # Convert to radians
        ax.bar(
            theta,
            group['Min'],
            width=0.3,
            color=plt.cm.viridis(combined_norm(group['Min'])),
            edgecolor='white',
            alpha=0.7,
            label='_nolegend_'
        )
        ax.bar(
            theta,
            group['Average'] - group['Min'],  # Adjusting the height to overlap with Min
            width=0.3,
            color=plt.cm.viridis(combined_norm(group['Average'])),
            edgecolor='white',
            alpha=0.7,
            bottom=group['Min'],
            label='_nolegend_'
        )
        ax.bar(
            theta,
            group['Max'] - group['Average'],  # Adjusting the height to overlap with Average
            width=0.3,
            color=plt.cm.viridis(combined_norm(group['Max'])),
            edgecolor='white',
            alpha=0.7,
            bottom=group['Average'],
            label='_nolegend_'
        )

        # Manually adjust radial position for overlaying bars
        ax.set_rmax(norm_max * 1.1)

        cbar = plt.colorbar(
            plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=combined_norm),
            ax=ax,
            pad=0.1,
            orientation='vertical',  # Change to 'horizontal' if needed
            aspect=20,  # Adjust the aspect ratio as needed
            shrink=0.8  # Adjust the shrink factor as needed
        )
        cbar.set_label('Wind Speed [m/s]')

        month_mapping = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }

        actual_month = month_mapping[month]
        plt.title(f'{concelho} - {actual_month} {year}', fontsize=20, y=1.05)
        print(f'Data for {concelho} - {actual_month} {year}:')
        print(group[['Direction', 'Min', 'Average', 'Max']])
        file_name = (f'{group["dicofre"].iloc[0]}_{concelho}_{year}_{actual_month}.png')
        plt.savefig(os.path.join('year_month_windroses', file_name), dpi=300, bbox_inches='tight', pad_inches=0.1)
        plt.close(fig)




#________________________________________________________________________WINDROSE TESTING________________________________________________________________________

def create_test_windrose():

    # Path to a shortened CSV file to test the code before processing the final CSV files
    file_path = "csv_files\\windrose_csv_data\\windrose_test.csv"

    # Read the CSV data using the updated file path
    data = pd.read_csv(file_path, header=None, skiprows=1, names=['Month', 'Year', 'Id_Estacao', 'dicofre', 'Concelho', 'Direction', 'Min', 'Max', 'Average'], encoding='utf-8')

    direction_mapping = {
        1.0: 0,
        2.0: 45.0,
        3.0: 90.0,
        4.0: 135.0,
        5.0: 180.0,
        6.0: 225.0,
        7.0: 270.0,
        8.0: 315.0
    }

    data['Direction'] = data['Direction'].map(direction_mapping)

    # Create a Windrose plot for each unique combination of Year, Month, and Concelho
    for (year, month, concelho), group in data.groupby(['Year', 'Month', 'Concelho']):
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(20, 10))

        # Set directional labels
        ax.set_theta_direction(-1)
        ax.set_theta_offset(0.5 * np.pi)
        ax.set_xticks(np.linspace(0, 2*np.pi, 8, endpoint=False))  # Adjust ticks for radians

        # Set custom direction labels
        direction_labels = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        ax.set_xticklabels(direction_labels)

        # Compute normalization limits for each windrose individually
        norm_min = 0
        norm_max = group[['Min', 'Average', 'Max']].max().max()
        combined_norm = plt.Normalize(norm_min, norm_max)

        # Plot three sets of bars for min, max, and average with manual radial positioning
        theta = group['Direction'].values * np.pi / 180  # Convert to radians
        ax.bar(
            theta,
            group['Min'],
            width=0.3,
            color=plt.cm.viridis(combined_norm(group['Min'])),
            edgecolor='white',
            alpha=0.7,
            label='_nolegend_'
        )
        ax.bar(
            theta,
            group['Average'] - group['Min'],  # Adjusting the height to overlap with Min
            width=0.3,
            color=plt.cm.viridis(combined_norm(group['Average'])),
            edgecolor='white',
            alpha=0.7,
            bottom=group['Min'],
            label='_nolegend_'
        )
        ax.bar(
            theta,
            group['Max'] - group['Average'],  # Adjusting the height to overlap with Average
            width=0.3,
            color=plt.cm.viridis(combined_norm(group['Max'])),
            edgecolor='white',
            alpha=0.7,
            bottom=group['Average'],
            label='_nolegend_'
        )

        # Manually adjust radial position for overlaying bars
        ax.set_rmax(norm_max * 1.1)

        cbar = plt.colorbar(
            plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=combined_norm),
            ax=ax,
            pad=0.1,
            orientation='vertical',  # Change to 'horizontal' if needed
            aspect=20,  # Adjust the aspect ratio as needed
            shrink=0.8  # Adjust the shrink factor as needed
        )
        cbar.set_label('Wind Speed [m/s]')

        month_mapping = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }

        actual_month = month_mapping[month]
        plt.title(f'{concelho} - {actual_month} {year}', fontsize=20, y=1.05)
        print(f'Data for {concelho} - {actual_month} {year}:')
        print(group[['Direction', 'Min', 'Average', 'Max']])
        file_name = (f'{group["dicofre"].iloc[0]}_{concelho}_{year}_{actual_month}.png')
        plt.savefig(os.path.join('year_month_windroses', file_name), dpi=300, bbox_inches='tight', pad_inches=0.1)
        plt.close(fig)
