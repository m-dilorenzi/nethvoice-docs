---
title: Bulk actions
sidebar_position: 5
---

# Bulk actions

The *Bulk actions* section allows you to manage and modify multiple extensions and phones simultaneously, improving operational efficiency when making changes to groups of users or devices.

## Bulk Extensions {#bulk-extensions-users}

The *Bulk Extensions/Users* feature allows you to modify multiple user extensions and their settings in a single operation.

### Selecting Extensions

To modify multiple extensions:

1. Use the **Select** dropdown menu to choose specific groups of extensions
2. Alternatively, check the checkboxes next to individual extensions in the list
3. Multiple extensions can be selected using a combination of both methods

### Modifying Extensions

Once you have selected the extensions to modify:

1. Click the **Modify** button
2. A configuration window will appear showing the available settings
3. The fields will display values only if all selected extensions have the same value for that field
4. If selected extensions have different values for a field, the field will remain empty

### Field Lock Status {#field-lock-status}

Each field has a lock icon on the right side:

- **Closed Lock**: The field will not be modified when you save
- **Open Lock**: The field value will be overwritten with the new value when you save

### Example

For example, if extensions 201 and 202 have different call group values:

- The call group field will appear empty
- With the lock closed, the existing values will remain unchanged when you save
- If you open the lock and save, the call group value will be overwritten for both extensions

## Bulk Phones {#bulk-phones}

The *Bulk Phones* feature allows you to manage and configure multiple phones simultaneously based on user groups or phone models.

### Selecting Phones

From **Applications > Bulk phones**, you can:

1. Select multiple phones using group criteria (user groups)
2. Filter by phone model
3. Once one or more selection criteria are applied, you can perform actions based on the selection

### Restart {#restart}

Provisioning settings are automatically applied to phones every night if automatic updates are enabled. If automatic updates are not enabled, you must manually restart the phones using this feature.

**Important**: Only phones that have completed SIP registration can be restarted from this page.

You can restart phones immediately or schedule the restart for a future time:

- **Restart now**: Immediately restart the selected phones
- **Delayed restart**: Schedule the restart for a specific time in the future

### Assign Model {#assign-model}

If the selected phones are from the same manufacturer, you can assign the same model to all of them using the **Assign model** button. This is useful when standardizing phone configurations across a group of users.