---
title: PBX Report
sidebar_position: 4
---

The unified NethVoice report provides a single web interface to consult:

- Queue reports
- Call and cost reports (CDR, Call Detail Record)

The report is accessible at `https://<server_name>/pbx-report`. Each user can log in with the same credentials used within NethVoice CTI. The tables and graphs displayed will be filtered based on the NethVoice CTI profile that the administrator has assigned to the user.

The report provides access only to historical data from the previous day, going back to the date of first PBX usage.

## Queue Report {#queue-report}

The queue report displays multiple information associated with PBX queues, such as agent data and work sessions, queue performance, geographic origin of calls, and wait time durations.

The various sections include inline documentation explaining the various features.

The module is divided into three main sections: **Data** and **Distribution** sections where statistical data is collected, and the **Graphs** section where this data is used to produce graphs that simplify analysis.

When accessing the module, you enter the **Dashboard**, which summarizes the most significant graphs.

### Data {#data}

#### Summary {#summary}

This section displays the calls received for each queue configured in NethVoice, divided into:

- **Handled calls**
  - Total
  - Maximum, minimum, and average wait time
  - Maximum, minimum, and average duration
  - Maximum and average position of entry into queue
- **Failed calls**
  - Total
  - Maximum, minimum, and average wait time
  - Maximum, minimum, and average position of entry and exit from queue

You can use the filter to create a more detailed search by time or by individual queue and export the result to an `.xls` file.

#### Per Agent {#per-agent}

This section displays the activities of agents in various queues, showing:

- Work time
- Pause time and actual pause time
- Calls answered
- Calls not answered
- Total conversation
- Calls per hour
- Occupancy percentage
- Maximum, minimum, and average duration of calls

You can use the filter to create a more detailed search by time or by individual agent and/or queue and export the result to an `.xls` file.

#### Per Session {#per-session}

This section displays the work and break sessions of queue agents, showing:

- Queue
- Agent
- Session type
- Session start and end time
- Duration
- Reason for break, if applicable

You can use the filter to create a more detailed search by time or by individual agent and/or queue and export the result to an `.xls` file.

#### Per Caller {#per-caller}

This section displays data related to calls entering queues, grouped by caller number.

You can use the filter to create a more detailed search by time or by individual queue or caller number and export the result to an `.xls` file.

#### Per Call {#per-call}

This section displays data related to calls entering queues, with the main purpose of showing their outcome. The following are displayed:

- Date
- Caller
- Called queue
- Agent (if it is a managed call)
- Position in queue
- Wait time
- Duration
- Outcome

You can use the filter to create a more detailed search by time or by individual queue or caller number and export the result to an `.xls` file.

#### Unhandled Calls {#unhandled-calls}

This section displays data related to calls that were not handled by operators.

You can use the filter to create a more detailed search by time or by individual queue or caller number and export the result to an `.xls` file.

#### IVR {#ivr}

This section displays calls that were directed to an IVR configured in NethVoice, showing:

- IVR name
- Choice made by the caller
- Total calls

You can use the filter to create a more detailed search by time or by individual inbound route and export the result to an `.xls` file.

#### Performance {#performance}

This section summarizes the performance of various queues, showing:

- Totals and percentages of calls:
  - Handled
  - Unhandled
  - Null
- Total wait and duration data

The quality of service offered by the queues is also displayed, grouping calls by wait time.

You can use the filter to create a more detailed search by time or by individual queue and export the result to an `.xls` file.

### Distribution {#distribution}

#### Hourly {#hourly}

In this section, incoming calls to queues are distributed throughout the daily time period and also divided by handled and unhandled calls.

You can use the filter to create a more detailed search by time or by individual queue and export the result to an `.xls` file.

#### Geographic {#geographic}

In this section, incoming calls to queues are grouped by geographic area and can be divided by Region, Province, or Area Code.

You can use the filter to create a more detailed search by time or by individual queue and export the result to an `.xls` file.

### Graphs {#graphs}

#### Load {#load}

This section displays graphs for the distribution of total incoming calls divided among various queues in the chosen time period and then divided by the chosen geographic area of origin.

#### Hourly {#graphs-hourly}

This section displays graphs for the hourly distribution of total incoming calls divided among various queues in the chosen time period.

#### Per Agent {#graphs-per-agent}

This section displays graphs for the total calls handled by queue agents in the chosen time period.

#### Per Zone {#per-zone}

This section displays graphs for the total incoming calls divided among various queues in the chosen time period based on the geographic area of origin.

#### Queue Position {#queue-position}

This section displays graphs for the position of entry of calls into the queue, divided among various queues.

#### Average Duration {#average-duration}

This section displays graphs for the average duration of incoming calls divided among various queues in the chosen time period based on entry time.

#### Average Wait {#average-wait}

This section displays graphs for the average wait of incoming calls divided among various queues in the chosen time period based on entry time.

#### Callback {#callback}

This section displays graphs for the calls made by agents successfully to numbers that had a failure in the queue.

## Call and Cost Report (CDR) {#cdr-report}

The CDR report displays aggregate and detailed information related to the call log. In addition to the **Dashboard** section, which presents some summary graphs, the following sections are present:

- **PBX Data**: information on incoming, outgoing, and internal calls to the PBX
- **Personal Data**: information on internal calls, received, or made by the logged-in user

The graphs in the **PBX Data** and **Personal Data** sections have the same structure, displaying:

- An expandable summary graph showing data on call totals and durations
- A tabular call log showing source number, destination number, call outcome, duration, and cost. By clicking the **Show Details** button, you can view additional details for each call

The first time you access the CDR report, a dialog box appears suggesting you configure call costs to include them in the report. For more information about call costs, see the [Administrator Manual - Report Settings](../../administrator-manual/configuration/report.md#costs) section.

The various sections include inline documentation explaining the various features.

## User Interface {#user-interface}

The user interface is common to both *queue report* and *CDR report*, and is organized in three main areas:

- Side menu
- Filters
- Graphs

:::note
Users with the `admin` account can access additional configuration options. See [Administrator Manual - Report Settings](../../administrator-manual/configuration/report.md) for more information.
:::

### Side Menu {#side-menu}

The side menu allows navigation of reports and contains:

- A selector to switch between queue report and CDR report views
- A search box to quickly find a view or graph of interest
- The complete structure of the current report (queues or CDR), organized into sections and views. Each section can aggregate a set of views or be self-contained (e.g., the *Dashboard* section)

### Filters {#filters}

The filters area allows you to configure the time interval and parameters to generate the report for the current view. The report generation can be started by clicking the **Search** button. The **Save Search** button allows you to save a specific filter configuration so it can be reused quickly.

In the top right corner of the filters area are the following buttons, through which you can (from left to right):

- Hide/show the filter panel
- Select the color scheme used by the graphs
- Access the report settings; this feature is only available if logged in with the `admin` user account
- Perform logout

### Graphs {#graphs-area}

The graphs area is the most interesting for the user and constitutes the body of the current view's report. Each graph can be exported in at least one of the following formats: CSV, PNG, and PDF. For readability reasons, some graphs display only the most relevant data: through the **Show Details** button you can access the complete set of graph data. Some types of graphs allow you to hide one or more data sets that you want to temporarily ignore: to do this, simply click on the relevant name in the graph legend.