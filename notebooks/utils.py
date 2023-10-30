import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)


# THESE ARE SOME UTILS FUNCTIONS FOR THE NOTEBOOKS;
# NOT PRODUCTION READY


# create y-var for goalscores variable
def create_goal_df(df, string_y_var, output_column_list):
    yvar_goals = df.loc[df["shot_outcome"] == string_y_var].reset_index()
    yvar_goals["goal"] = 1
    yvar_goals["y_minute"] = yvar_goals["minute"]
    yvar_goals["peil_minute"] = yvar_goals["minute"] - 1
    df_goals = yvar_goals[output_column_list]
    return df_goals


# create y-var for no goals variable
def create_no_goals_df(df, df_goals, uniek_id_list, column_selection):
    df_no_goals_total = []
    for uniekid in uniek_id_list:
        df_per_match = df.loc[df["uniekid"] == uniekid]
        last_minute_game = max(df_per_match["minute"])
        goals = df_goals.loc[df_goals["uniekid"] == uniekid]
        goals_minutes = goals["y_minute"].unique()
        df_no_goals = pd.DataFrame(np.arange(1, last_minute_game))
        df_no_goals = df_no_goals.rename(columns={0: "minute"})
        df_no_goals = df_no_goals.loc[
            ~df_no_goals["minute"].isin(goals_minutes)
        ]  # only select the minutes in which no goal was scored
        df_no_goals["goal"] = 0
        df_no_goals["y_minute"] = df_no_goals["minute"]
        df_no_goals["peil_minute"] = df_no_goals["minute"] - 1
        df_no_goals["uniekid"] = uniekid
        df_no_goals["match_id"] = df_no_goals["uniekid"].astype(str).str[:7]
        df_no_goals = df_no_goals[column_selection]
        df_no_goals_total.append(df_no_goals)
    return pd.concat(df_no_goals_total)


# create x-var dataframe:
def get_events_per_id(df, events_selection_list, uniek_id_list):
    events_all_matches_select = []
    for uniekid in uniek_id_list:
        events_per_match_select = df.loc[df["uniekid"] == uniekid]
        events_per_match_select = events_per_match_select.loc[
            events_per_match_select["minute"] >= 1
        ]  # remove starting positions
        events_per_match_select = events_per_match_select[
            events_selection_list
        ]  # noqa:E501
        events_per_match_select = events_per_match_select.loc[
            ~events_per_match_select["location"].isnull()
        ]  # drop substitutes
        events_to_drop = ["Half Start", "Half End"]
        events_per_match_select = events_per_match_select.loc[
            ~events_per_match_select["type"].isin(events_to_drop)
        ]
        events_all_matches_select.append(events_per_match_select)
    return pd.concat(events_all_matches_select)


# recreate features in x-var dataframe:
def events_feature_engineering(df):
    location_x = []
    location_y = []
    for k, v in df.iterrows():
        x = v["location"][0]
        y = v["location"][1]
        location_x.append(x)
        location_y.append(y)

    df["location_x"] = location_x
    df["location_y"] = location_y
    df = df.drop("location", axis=1)
    df.loc[df["location_x"] >= 60, "aanvallende_helft"] = 1
    df.loc[df["location_x"] < 60, "aanvallende_helft"] = 0
    df.loc[df["location_x"] >= 90, "aanvallend_kwart"] = 1
    df.loc[df["location_x"] < 90, "aanvallend_kwart"] = 0
    df["in_de_16"] = 0
    df.loc[
        (df["location_x"] >= 102.62)
        & (df["location_y"] >= 18)
        & (df["location_y"] <= 62),
        "in_de_16",
    ] = 1
    df.loc[df["under_pressure"] == True, "under_pressure"] = 1  # noqa: E712
    df.loc[df["under_pressure"] != 1, "under_pressure"] = 0
    df = df.drop("location_x", axis=1)
    df = df.drop("location_y", axis=1)
    return df


# aggregate-events
def aggregate_events_per_minute(df, groupby_columns, agg_type_max):
    x_vars = df.drop(groupby_columns, axis=1).columns.to_list()
    total_sum = []
    for column in x_vars:
        if agg_type_max:
            col_sum = df.groupby(groupby_columns)[
                column
            ].max()  # get max of feature # noqa:E501
        else:
            col_sum = df.groupby(groupby_columns)[
                column
            ].sum()  # get sum of feature # noqa:E501
        total_sum.append(col_sum)
    df_agg = pd.concat(total_sum, axis=1).reset_index()
    return df_agg


# evaluate models
def evaluate_model(name, model, features, labels):
    pred = model.predict(features)
    accuracy = round(accuracy_score(labels, pred), 3)
    precision = round(precision_score(labels, pred), 3)
    recall = round(recall_score(labels, pred), 3)
    f1 = round(f1_score(labels, pred), 3)
    roc = round(roc_auc_score(labels, pred), 3)

    print(
        "{} -- Accuracy:{} / Precision:{} / Recall:{} / F1:{} / ROC:{} ".format(  # noqa:E501
            name, accuracy, precision, recall, f1, roc
        )
    )
