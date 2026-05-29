/**
 * StoreHub Creative Testing — Weekly Action Plan Generator
 *
 * Setup: In Google Sheets, go to Extensions → Apps Script
 * Paste this entire file, save, then reload the sheet.
 * A "Action Plan" menu will appear in the menu bar.
 */

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Action Plan')
    .addItem('Generate Weekly Actions', 'generateActionPlan')
    .addToUi();
}

function generateActionPlan() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const themeSummary = ss.getSheetByName('Theme Summary');
  const creativeVariants = ss.getSheetByName('Creative Variants');
  const helpers = ss.getSheetByName('Helpers');
  const weeklyPerf = ss.getSheetByName('Weekly Performance');

  if (!themeSummary || !helpers) {
    SpreadsheetApp.getUi().alert('Missing required tabs: Theme Summary or Helpers');
    return;
  }

  // Get or create Action Plan tab
  let sheet = ss.getSheetByName('Action Plan');
  if (!sheet) {
    sheet = ss.insertSheet('Action Plan');
  }

  // Read week info from Helpers
  const weekStart = helpers.getRange('B2').getDisplayValue();
  const weekEnd = helpers.getRange('B3').getDisplayValue();

  // ===== READ THEME SUMMARY =====
  const themes = readThemeSummary(themeSummary);

  // ===== READ CREATIVE VARIANTS =====
  const variants = creativeVariants ? readCreativeVariants(creativeVariants) : [];

  // ===== READ WEEKLY PERFORMANCE (WoW) =====
  const wow = weeklyPerf ? readWeeklyPerformance(weeklyPerf) : null;

  // ===== GENERATE RECOMMENDATIONS =====
  const actions = generateRecommendations(themes, variants, wow);

  // ===== WRITE TO SHEET =====
  writeActionPlan(sheet, actions, weekStart, weekEnd, themes);

  SpreadsheetApp.getUi().alert('Generated ' + actions.length + ' action items for the week.');
}


// ───────────────────────────────────────────
// DATA READERS
// ───────────────────────────────────────────

function readThemeSummary(sheet) {
  const data = sheet.getDataRange().getValues();
  let headerRow = -1;
  for (let i = 0; i < data.length; i++) {
    if (data[i][0] && data[i][0].toString().toUpperCase().trim() === 'THEME') {
      headerRow = i;
      break;
    }
  }
  if (headerRow === -1) return [];

  const headers = data[headerRow].map(function(h) { return h.toString().toUpperCase().trim(); });
  const col = function(name) { return headers.indexOf(name); };

  var themes = [];
  for (var i = headerRow + 1; i < data.length; i++) {
    var row = data[i];
    var theme = row[col('THEME')];
    if (!theme || theme === '') break;

    themes.push({
      name: String(theme),
      country: String(row[col('COUNTRY')] || ''),
      variants: Number(row[col('# VARIANTS')]) || 0,
      spend: Number(row[col('TOTAL SPEND')]) || 0,
      impressions: Number(row[col('IMPRESSIONS')]) || 0,
      clicks: Number(row[col('CLICKS')]) || 0,
      ctr: parsePercent(row[col('CTR%')]),
      leads: Number(row[col('LEADS')]) || 0,
      mql: Number(row[col('MQL')]) || 0,
      mqlRate: parsePercent(row[col('MQL%')]),
      sql: Number(row[col('SQL')]) || 0,
      sqlRate: parsePercent(row[col('SQL%')]),
      won: Number(row[col('WON')]) || 0,
      cpl: Number(row[col('CPL')]) || 0,
      cpmql: Number(row[col('CPMQL')]) || 0,
    });
  }
  return themes;
}

function readCreativeVariants(sheet) {
  const data = sheet.getDataRange().getValues();
  let headerRow = -1;
  for (let i = 0; i < data.length; i++) {
    if (data[i][0] && data[i][0].toString().toUpperCase().trim() === 'AD NAME') {
      headerRow = i;
      break;
    }
  }
  if (headerRow === -1) return [];

  const headers = data[headerRow].map(function(h) { return h.toString().toUpperCase().trim(); });
  const col = function(name) { return headers.indexOf(name); };

  var variants = [];
  for (var i = headerRow + 1; i < data.length; i++) {
    var row = data[i];
    var adName = row[col('AD NAME')];
    if (!adName || adName === '') break;

    variants.push({
      adName: String(adName),
      theme: String(row[col('THEME')] || ''),
      spend: Number(row[col('SPEND')]) || 0,
      impressions: Number(row[col('IMPRESSIONS')]) || 0,
      clicks: Number(row[col('CLICKS')]) || 0,
      ctr: parsePercent(row[col('CTR%')]),
      leads: Number(row[col('LEADS')]) || 0,
      mql: Number(row[col('MQL')]) || 0,
      cpl: Number(row[col('CPL')]) || 0,
    });
  }
  return variants;
}

function readWeeklyPerformance(sheet) {
  const data = sheet.getDataRange().getValues();
  // Find "This Week" and "Last Week" rows
  var thisWeek = null, lastWeek = null;
  for (var i = 0; i < data.length; i++) {
    var label = String(data[i][0]).toLowerCase().trim();
    if (label === 'this week') thisWeek = data[i];
    if (label === 'last week') lastWeek = data[i];
  }
  if (!thisWeek || !lastWeek) return null;

  // Find header row for column mapping
  let headerRow = -1;
  for (let i = 0; i < data.length; i++) {
    if (data[i][0] && data[i][0].toString().toUpperCase().trim() === 'METRIC') {
      headerRow = i;
      break;
    }
  }
  if (headerRow === -1) return null;

  const headers = data[headerRow].map(function(h) { return h.toString().toUpperCase().trim(); });
  const col = function(name) { return headers.indexOf(name); };

  return {
    thisWeek: {
      spend: Number(thisWeek[col('SPEND')]) || 0,
      impressions: Number(thisWeek[col('IMPRESSIONS')]) || 0,
      clicks: Number(thisWeek[col('CLICKS')]) || 0,
      leads: Number(thisWeek[col('LEADS')]) || 0,
      mql: Number(thisWeek[col('MQL')]) || 0,
      sql: Number(thisWeek[col('SQL')]) || 0,
    },
    lastWeek: {
      spend: Number(lastWeek[col('SPEND')]) || 0,
      impressions: Number(lastWeek[col('IMPRESSIONS')]) || 0,
      clicks: Number(lastWeek[col('CLICKS')]) || 0,
      leads: Number(lastWeek[col('LEADS')]) || 0,
      mql: Number(lastWeek[col('MQL')]) || 0,
      sql: Number(lastWeek[col('SQL')]) || 0,
    }
  };
}


// ───────────────────────────────────────────
// RECOMMENDATION ENGINE
// ───────────────────────────────────────────

function generateRecommendations(themes, variants, wow) {
  var actions = [];

  // Averages for comparison
  var themesWithLeads = themes.filter(function(t) { return t.leads > 0 && t.spend > 0; });
  var avgCPL = themesWithLeads.length > 0
    ? themesWithLeads.reduce(function(s, t) { return s + t.cpl; }, 0) / themesWithLeads.length
    : 0;
  var totalSpend = themes.reduce(function(s, t) { return s + t.spend; }, 0);

  // Sort winners by CPL (best first)
  var byBestCPL = themesWithLeads.slice().sort(function(a, b) { return a.cpl - b.cpl; });

  // Wasted spend — high spend, 0 leads
  var wastedSpend = themes.filter(function(t) { return t.spend > 20 && t.leads === 0; })
    .sort(function(a, b) { return b.spend - a.spend; });

  // ── P1: SCALE WINNERS ──
  if (byBestCPL.length > 0) {
    var best = byBestCPL[0];
    actions.push({
      priority: 'P1',
      category: 'Scale',
      action: "Increase daily budget on '" + best.name + "' by 20%",
      reasoning: "Best CPL at RM" + best.cpl.toFixed(2) + " with " + best.leads + " leads" +
        (best.mqlRate > 0 ? ", " + best.mqlRate.toFixed(0) + "% MQL rate" : ""),
    });
  }

  // High MQL rate themes
  themesWithLeads.forEach(function(theme) {
    if (theme.mqlRate >= 80 && theme !== byBestCPL[0]) {
      actions.push({
        priority: 'P1',
        category: 'Scale',
        action: "Prioritize '" + theme.name + "' — exceptional lead quality",
        reasoning: theme.mqlRate.toFixed(0) + "% MQL rate, " + theme.mql + " MQLs from " + theme.leads + " leads",
      });
    }
  });

  // ── P1: KILL UNDERPERFORMERS ──
  wastedSpend.forEach(function(theme) {
    if (theme.spend >= 50) {
      actions.push({
        priority: 'P1',
        category: 'Kill',
        action: "Pause '" + theme.name + "' — wasting budget",
        reasoning: "RM" + theme.spend.toFixed(2) + " spent with 0 leads" +
          (theme.clicks > 0 ? ", " + theme.clicks + " clicks but no conversions" : ", 0 clicks"),
      });
    }
  });

  // Kill specific variants within performing themes
  if (variants.length > 0) {
    var variantsByTheme = {};
    variants.forEach(function(v) {
      if (!variantsByTheme[v.theme]) variantsByTheme[v.theme] = [];
      variantsByTheme[v.theme].push(v);
    });

    Object.keys(variantsByTheme).forEach(function(themeName) {
      var themeVariants = variantsByTheme[themeName];
      var themeHasLeads = themeVariants.some(function(v) { return v.leads > 0; });

      if (themeHasLeads) {
        themeVariants.forEach(function(v) {
          if (v.spend > 30 && v.leads === 0 && v.clicks === 0) {
            var shortName = v.adName.split('_').slice(-1)[0] || v.adName;
            actions.push({
              priority: 'P1',
              category: 'Kill',
              action: "Pause variant '" + shortName.trim() + "' in " + themeName,
              reasoning: "RM" + v.spend.toFixed(2) + " spent, 0 clicks — reallocate to winning variants",
            });
          }
        });
      }
    });
  }

  // ── P2: CREATIVE REFRESH ──
  themes.forEach(function(theme) {
    if (theme.spend > 100 && theme.leads === 0) {
      actions.push({
        priority: 'P2',
        category: 'Creative',
        action: "Create 2 new '" + theme.name + "' variants with different angles",
        reasoning: "RM" + theme.spend.toFixed(2) + " spend, 0 leads — creative fatigue or poor message-market fit",
      });
    }
  });

  // Low CTR
  themes.forEach(function(theme) {
    if (theme.impressions > 1000 && theme.ctr > 0 && theme.ctr < 0.5) {
      actions.push({
        priority: 'P2',
        category: 'Creative',
        action: "Refresh creative for '" + theme.name + "' — low engagement",
        reasoning: "CTR at " + theme.ctr.toFixed(2) + "% across " + theme.impressions.toLocaleString() + " impressions",
      });
    }
  });

  // ── P2: OPTIMIZE ──
  themesWithLeads.forEach(function(theme) {
    if (avgCPL > 0 && theme.cpl > avgCPL * 1.5) {
      actions.push({
        priority: 'P2',
        category: 'Optimize',
        action: "Review targeting for '" + theme.name + "' — CPL above average",
        reasoning: "CPL RM" + theme.cpl.toFixed(2) + " vs avg RM" + avgCPL.toFixed(2) + " — narrow audience or adjust bid",
      });
    }
  });

  // Low variant diversity
  themes.forEach(function(theme) {
    if (theme.variants <= 1 && theme.spend > 0) {
      actions.push({
        priority: 'P2',
        category: 'Test',
        action: "Add 2 more variants for '" + theme.name + "'",
        reasoning: "Only " + theme.variants + " variant running — need 3+ for meaningful A/B testing",
      });
    }
  });

  // ── P2: WOW ALERTS ──
  if (wow) {
    var tw = wow.thisWeek, lw = wow.lastWeek;

    // Lead drop
    if (lw.leads > 0 && tw.leads < lw.leads) {
      var dropPct = ((lw.leads - tw.leads) / lw.leads * 100).toFixed(0);
      if (Number(dropPct) >= 30) {
        actions.push({
          priority: 'P2',
          category: 'Investigate',
          action: "Leads dropped " + dropPct + "% WoW — diagnose cause",
          reasoning: tw.leads + " leads this week vs " + lw.leads + " last week. Check: budget changes, audience saturation, creative fatigue",
        });
      }
    }

    // Spend increase without lead increase
    if (lw.spend > 0 && tw.spend > lw.spend * 1.2 && tw.leads <= lw.leads) {
      actions.push({
        priority: 'P2',
        category: 'Optimize',
        action: "Spend up but leads flat/down — check efficiency",
        reasoning: "Spend: RM" + tw.spend.toFixed(0) + " vs RM" + lw.spend.toFixed(0) + " last week, but leads " + tw.leads + " vs " + lw.leads,
      });
    }

    // Lead surge — good signal
    if (lw.leads > 0 && tw.leads > lw.leads * 1.5) {
      var surgePct = ((tw.leads - lw.leads) / lw.leads * 100).toFixed(0);
      actions.push({
        priority: 'P2',
        category: 'Scale',
        action: "Leads up " + surgePct + "% WoW — identify and scale what's working",
        reasoning: tw.leads + " leads this week vs " + lw.leads + " last week. Double down on winning themes",
      });
    }
  }

  // ── P3: FOLLOW-UPS ──
  themes.forEach(function(theme) {
    if (theme.sql > 0 && theme.won === 0) {
      actions.push({
        priority: 'P3',
        category: 'Follow-up',
        action: "Follow up on " + theme.sql + " SQL(s) from '" + theme.name + "'",
        reasoning: theme.sql + " SQL, 0 Won — check sales pipeline and deal stage",
      });
    }
  });

  // Themes with RM0 spend (paused or disapproved)
  themes.forEach(function(theme) {
    if (theme.spend === 0 && theme.variants > 0) {
      actions.push({
        priority: 'P3',
        category: 'Review',
        action: "Check if '" + theme.name + "' ads are active",
        reasoning: "RM0 spend with " + theme.variants + " variants — may be paused or disapproved",
      });
    }
  });

  // Sort by priority
  var priorityOrder = { 'P1': 1, 'P2': 2, 'P3': 3 };
  actions.sort(function(a, b) {
    return (priorityOrder[a.priority] || 99) - (priorityOrder[b.priority] || 99);
  });

  return actions;
}


// ───────────────────────────────────────────
// SHEET WRITER
// ───────────────────────────────────────────

function writeActionPlan(sheet, actions, weekStart, weekEnd, themes) {
  // Preserve completed items from previous weeks
  var completedItems = getCompletedItems(sheet);

  sheet.clear();

  // ── TITLE ──
  sheet.getRange('A1').setValue('STOREHUB \u2014 CREATIVE TESTING | WEEKLY ACTION PLAN');
  sheet.getRange('A1:F1').merge();
  sheet.getRange('A1').setFontSize(13).setFontWeight('bold').setBackground('#2f2922').setFontColor('#ffffff');

  // ── WEEK INFO ──
  sheet.getRange('A2').setValue('Week: ' + weekStart + ' \u2013 ' + weekEnd + '  |  Generated: ' + Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'dd-MMM-yyyy HH:mm'));
  sheet.getRange('A2:F2').merge();
  sheet.getRange('A2').setFontSize(9).setFontColor('#666666');

  // ── SUMMARY STATS ──
  var totalSpend = themes.reduce(function(s, t) { return s + t.spend; }, 0);
  var totalLeads = themes.reduce(function(s, t) { return s + t.leads; }, 0);
  var totalMQL = themes.reduce(function(s, t) { return s + t.mql; }, 0);
  var totalSQL = themes.reduce(function(s, t) { return s + t.sql; }, 0);
  var p1Count = actions.filter(function(a) { return a.priority === 'P1'; }).length;

  sheet.getRange('A3').setValue(
    totalLeads + ' leads  |  ' + totalMQL + ' MQL  |  ' + totalSQL + ' SQL  |  RM' + totalSpend.toFixed(2) + ' spend  |  ' +
    actions.length + ' actions (' + p1Count + ' urgent)'
  );
  sheet.getRange('A3:F3').merge();
  sheet.getRange('A3').setFontSize(9).setBackground('#fff3e0').setFontWeight('bold');

  // ── CURRENT WEEK ACTIONS ──
  var headerRow = 5;
  var headers = ['\u2610', 'PRIORITY', 'CATEGORY', 'ACTION ITEM', 'REASONING', 'WEEK'];
  sheet.getRange(headerRow, 1, 1, headers.length).setValues([headers]);
  sheet.getRange(headerRow, 1, 1, headers.length)
    .setFontWeight('bold')
    .setBackground('#ff9419')
    .setFontColor('#ffffff')
    .setHorizontalAlignment('center');
  sheet.getRange(headerRow, 4).setHorizontalAlignment('left');
  sheet.getRange(headerRow, 5).setHorizontalAlignment('left');

  var dataStartRow = headerRow + 1;
  var weekLabel = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'dd-MMM');

  var priorityColors = { 'P1': '#ffebee', 'P2': '#fff8e1', 'P3': '#f1f8e9' };
  var priorityTextColors = { 'P1': '#c62828', 'P2': '#f57f17', 'P3': '#558b2f' };

  if (actions.length === 0) {
    sheet.getRange(dataStartRow, 4).setValue('All themes performing within normal range — no urgent actions needed');
    sheet.getRange(dataStartRow, 4).setFontStyle('italic').setFontColor('#999999');
  } else {
    for (var i = 0; i < actions.length; i++) {
      var row = dataStartRow + i;
      var action = actions[i];

      // Checkbox
      sheet.getRange(row, 1).insertCheckboxes();

      // Values
      sheet.getRange(row, 2).setValue(action.priority);
      sheet.getRange(row, 3).setValue(action.category);
      sheet.getRange(row, 4).setValue(action.action);
      sheet.getRange(row, 5).setValue(action.reasoning);
      sheet.getRange(row, 6).setValue(weekLabel);

      // Priority styling
      sheet.getRange(row, 2)
        .setBackground(priorityColors[action.priority] || '#ffffff')
        .setFontColor(priorityTextColors[action.priority] || '#000000')
        .setFontWeight('bold')
        .setHorizontalAlignment('center');

      sheet.getRange(row, 3).setHorizontalAlignment('center');
      sheet.getRange(row, 6).setHorizontalAlignment('center').setFontColor('#999999');

      // Alternate row shading
      if (i % 2 === 1) {
        sheet.getRange(row, 3, 1, 4).setBackground('#fafafa');
      }
    }
  }

  // ── COMPLETED ACTIONS LOG (from previous weeks) ──
  if (completedItems.length > 0) {
    var logHeaderRow = dataStartRow + actions.length + 2;
    sheet.getRange(logHeaderRow, 1).setValue('COMPLETED ACTIONS (Previous Weeks)');
    sheet.getRange(logHeaderRow, 1, 1, 6).merge();
    sheet.getRange(logHeaderRow, 1)
      .setFontWeight('bold')
      .setBackground('#e8f5e9')
      .setFontColor('#2e7d32');

    for (var j = 0; j < completedItems.length; j++) {
      var cRow = logHeaderRow + 1 + j;
      sheet.getRange(cRow, 1).insertCheckboxes();
      sheet.getRange(cRow, 1).setValue(true);
      sheet.getRange(cRow, 2).setValue(completedItems[j][0]); // priority
      sheet.getRange(cRow, 3).setValue(completedItems[j][1]); // category
      sheet.getRange(cRow, 4).setValue(completedItems[j][2]); // action
      sheet.getRange(cRow, 5).setValue(completedItems[j][3]); // reasoning
      sheet.getRange(cRow, 6).setValue(completedItems[j][4]); // week

      sheet.getRange(cRow, 1, 1, 6).setFontColor('#999999');
    }
  }

  // ── COLUMN WIDTHS ──
  sheet.setColumnWidth(1, 30);
  sheet.setColumnWidth(2, 70);
  sheet.setColumnWidth(3, 100);
  sheet.setColumnWidth(4, 420);
  sheet.setColumnWidth(5, 380);
  sheet.setColumnWidth(6, 80);

  // Freeze header
  sheet.setFrozenRows(headerRow);
}

function getCompletedItems(sheet) {
  var completed = [];
  try {
    var data = sheet.getDataRange().getValues();
    for (var i = 0; i < data.length; i++) {
      // Check if checkbox is TRUE (completed)
      if (data[i][0] === true) {
        completed.push([
          data[i][1], // priority
          data[i][2], // category
          data[i][3], // action
          data[i][4], // reasoning
          data[i][5], // week
        ]);
      }
    }
  } catch (e) {
    // Sheet might be empty or have no data
  }
  return completed;
}


// ───────────────────────────────────────────
// HELPERS
// ───────────────────────────────────────────

function parsePercent(val) {
  if (typeof val === 'number') return val * (val < 1 ? 100 : 1);
  var str = String(val).replace('%', '').trim();
  var num = Number(str);
  return isNaN(num) ? 0 : num;
}
