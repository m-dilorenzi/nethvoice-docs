---
title: PBX Report
sidebar_position: 12
---

The unified NethVoice report provides a single web interface to view:

- Queue reports
- Call and cost reports (CDR, Call Detail Record)

The report is accessible at `https://<server_name>/pbx-report`. Each user can log in with the same credentials used within NethVoice CTI. The tables and graphs displayed will be filtered based on the NethVoice CTI profile assigned to the user. When logging in with the NethVoice `admin` user, it is always possible to view all data.

The report provides access only to historical data from the previous day, going back to the date of first PBX usage. Every night a process processes the day's events and makes them available for displaying graphs and tables. Therefore, at the end of the first installation, you must wait until the next day to view the report.

The report is available with the installation of the NethVoice instance.

For details on reports, refer to the [User Manual - Report](../../user-manual/nethcti/report.md) section.

Settings are reserved for the administrator.

## Settings {#settings}

Report settings are accessible by clicking the gear icon button in the toolbar at the top right. The button is visible only when logged in with the `admin` user account.

Settings are organized in the following sections:

- General
- Destinations
- Costs
- Reset Settings

### General {#general}

In this section you can configure the following settings:

- **Working hours start/end**: This information is used by graphs that track data based on daily time periods
- **Maximum number of results**: Indicates how many results can be displayed by a tabular graph. If this limit is reached, a warning icon appears next to the graph title
- **Null call duration**: Calls with a duration less than or equal to this value are considered null
- **Currency**: Used to display call costs

### Destinations {#destinations}

Destinations are used to calculate call costs. The default configuration includes the following destinations:

- `National`: National numbers
- `Mobile`: Mobile numbers
- `International`: International numbers
- `Emergency`: Emergency numbers
- `PayNumber`: Premium numbers

You can add new destinations or remove existing ones.

By expanding the **Configure destination prefixes** option, you can configure the destination of a call using the phone number prefix. Since each defined prefix can have variable length and overlaps are therefore possible, the destination of a phone number is determined by selecting the most specific prefix (i.e., the *longest*). For example, assuming you associate the prefix `0039` with the `National` destination, and the prefix `00393` with the `Mobile` destination, an outgoing call to the number `00393401234567` will have the `Mobile` destination, because the prefix `00393` is more specific than the prefix `0039`.

### Costs {#costs}

After configuring the call destinations and destination prefixes, you can configure call costs. The cost of a call is determined by the PBX trunk and the destination of the call. To configure a new cost, simply specify the trunk, the destination, and the relative rate per minute.

#### Example of configuring a new cost {#example-new-cost}

Suppose you have activated a telephone contract on a PBX trunk named `trunk_1` according to which calls to Spain are charged at 0.01 EUR per minute. To ensure that the cost of these calls is calculated and displayed in the report, follow these steps:

- Access the report with the `admin` user account
- Access the settings
- Define a new destination, naming it for example `Spain`
- Configure a new destination prefix, indicating the Spanish national prefix (`0034` or `+34`, depending on how the PBX was configured) and selecting `Spain` as the destination
- Configure a new cost, selecting the trunk `trunk_1`, the destination `Spain`, and specifying `0.01 EUR` as the cost per minute

From this point on, every night a process will calculate the costs of calls made from the `trunk_1` trunk to Spain. Call costs are therefore available from the day after configuration.

### Reset Settings {#reset-settings}

**Warning**

Resetting settings is irreversible

This section contains a button to reset all settings to their default values. Clicking the button and confirming the choice will reset all settings contained in the **General** section, all destinations, destination prefixes, and all cost configurations will be deleted. 
